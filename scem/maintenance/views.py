from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404,render,redirect
from .models import Order, Unit
from django.contrib.auth import get_user_model
from .forms import OrderForm
from django.contrib import messages
from django.db.models import Sum
from django.db.models.functions import ExtractYear, ExtractMonth
import datetime
# Create your views here.
@login_required
def order_list(request, unit_slug=None):
    unit = None
    unities = Unit.objects.all()
    orders = Order.objects.filter(status="EF")
    if unit_slug:
        unit = get_object_or_404(Unit, slug=unit_slug)
        orders = orders.filter(unit=unit)
    return render(
        request,
        'maintenance/order/list.html',
        {
            'unit':unit,
            'unities': unities,
            'orders': orders,
        }
    )

@login_required
def order_detail(request, id, slug):
    User = get_user_model()
    users = User.objects.all()
    order = get_object_or_404(
        Order, id=id, slug=slug, status='EF'
    )

    if request.method == "POST":

        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form1 = form.save(commit=False)
            end_date = datetime.date.fromisoformat(str(form.cleaned_data['end_date']))
            start_date = datetime.date.fromisoformat(str(form.cleaned_data['start_date']))
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            start = datetime.datetime.combine(start_date, start_time)
            end = datetime.datetime.combine(end_date, end_time)
            hours = (end-start).total_seconds()/3600
            over_time = 0
            normal_time = 0
            if start.day == end.day:
                if start < datetime.datetime.combine(start_date,datetime.datetime.strptime("08:00", "%H:%M").time()):
                    if end < datetime.datetime.combine(start_date,
                                                         datetime.datetime.strptime("08:00", "%H:%M").time()):
                        over_time = (end - start).total_seconds()/3600
                    elif end < datetime.datetime.combine(start_date,
                                                         datetime.datetime.strptime("18:00", "%H:%M").time()):
                        over_time = (datetime.datetime.combine(start_date,datetime.datetime.strptime("08:00", "%H:%M").time())-start).total_seconds()/3600
                    else:
                        over_time = (datetime.datetime.combine(start_date, datetime.datetime.strptime("08:00",
                                                                                                      "%H:%M").time()) - start).total_seconds() / 3600 + (end - datetime.datetime.combine(start_date, datetime.datetime.strptime("18:00",
                                                                                                      "%H:%M").time())).total_seconds() / 3600
                elif start < datetime.datetime.combine(start_date,datetime.datetime.strptime("18:00", "%H:%M").time()):
                    if end < datetime.datetime.combine(start_date,
                                                         datetime.datetime.strptime("18:00", "%H:%M").time()):
                        over_time = (end - start).total_seconds() / 3600
                    else:
                        over_time = (end - datetime.datetime.combine(start_date, datetime.datetime.strptime("18:00",
                                                                                                "%H:%M").time())).total_seconds() / 3600
                else:
                    over_time = (end - start).total_seconds() / 3600


            normal_time = (end - start).total_seconds() / 3600 - over_time
            form1.normal_time  = normal_time
            form1.over_time = over_time
            form1.save()
            messages.success(
                request,
                'Ordem de serviço atualizada com sucesso'
            )
            return redirect("/")
    return render(
                request,
                'maintenance/order/detail.html',
                {
                 'order': order,
                 'users': users
                 }
            )

@login_required
def report(request):
    User = get_user_model()
    users = User.objects.values('id', 'first_name', 'last_name')
    summary = (Order.objects.select_related('technician').values('technician','technician__first_name','technician__last_name',
                                   month = ExtractMonth('end_date'),
                                   year = ExtractYear('end_date')
                                    ).order_by('technician__first_name',
                                               'technician__last_name',
                                               'year',
                                               'month'
                                               ).annotate(total_normal_time=Sum('normal_time'),
                                                          total_over_time=Sum('over_time')))
    return render(
        request,
        'maintenance/order/summary.html',
        {
            'summary': summary,
            'users': users
        }
    )