from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404,render
from .models import Order, Unit

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
    order = get_object_or_404(
    Order, id=id, slug=slug, status='EF'
    )
    return render(
        request,
        'maintenance/order/detail.html',
        {'order': order}
    )