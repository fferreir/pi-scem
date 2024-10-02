from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404,render
from .models import Order, Unit

# Create your views here.
@login_required
def order_list(request, unit_slug=None):
    unit = None
    unities = Unit.objects.all()
    orders = Order.objects.filter(status=True)
    if unit_slug:
        unit = get_object_or_404(Unit, slug=unit_slug)
        orders = orders.filter(uniti=unit)
    return render(
        request,
        'maintenance/unit/list.html',
        {
            'unit': unit,
            'unities': unities,
            'orders': orders
        }
    )