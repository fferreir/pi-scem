from django.urls import path
from . import views

app_name = 'maintenance'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('<slug:unit_slug>/', views.order_list, name='order_list_by_unit'),
    path('<int:id>/<slug:slug>/', views.order_detail, name='order_detail'),
]