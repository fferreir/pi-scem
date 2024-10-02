from django.contrib import admin

# Register your models here.
from .models import Order, Unit

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'unit',
        'technician',
        'tag',
        'description',
        'start_date',
        'start_time',
        'end_date',
        'end_time',
        'created',
        'updated',
        'status',
        'slug',
    ]
    prepopulated_fields = {'slug': ('unit',)}

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'manager',
        'active',
        'created',
        'slug',
    ]
    list_filter = ['name', 'manager', 'created']
    list_editable = ['manager',]
    prepopulated_fields = {'slug': ('name',)}