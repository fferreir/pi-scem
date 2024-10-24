from django.forms import ModelForm

from maintenance.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
