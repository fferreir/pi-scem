from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Unit(models.Model):
    name = models.CharField(max_length=200)
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='manager'
    )
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
        models.Index(fields=['name']),
        ]
        verbose_name = 'order'
        verbose_name_plural = 'unities'

    def get_absolute_url(self):
        return reverse(
            'maintenance:order_list_by_unit', args = [self.slug])

    def __str__(self):
        return self.name

class Order(models.Model):
    class Status(models.TextChoices):
        FILA = 'EF', 'Em fila'
        ATENDIMENTO = 'EA', 'Em atendimento'
        FINALIZADO = 'FI', 'Finalizado'

    unit = models.ForeignKey(
        Unit,
        related_name = 'orders',
        on_delete = models.CASCADE
    )
    requestor = models.CharField(max_length=200)
    addr = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    technician = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'orders',
        null = True,
    )
    tag = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    start_time = models.TimeField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    end_time = models.TimeField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status,
                              default=Status.FILA
                              )
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['technician']),
            models.Index(fields=['created']),
        ]
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def get_absolute_url(self):
        return reverse('maintenance:order_detail', args=[self.id, self.slug])

    def __str__(self):
        return str(self.id)