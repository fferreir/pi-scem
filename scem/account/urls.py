from django.contrib.auth import views as auth_views
from django.urls import include,path
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('edit/', views.edit, name='edit'),
]
