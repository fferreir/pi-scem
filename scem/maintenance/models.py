from django.db import models
from django.conf import settings

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
        verbose_name = 'unidade'
        verbose_name_plural = 'unidades'

    def__str__(self):
        return self.name

class Maintenance(models.Model):
    class Status(models.TextChoices):
        FILA = 'EF', 'Em fila'
        ATENDIMENTO = 'EA', 'Em atendimento'
        FINALIZADO = 'FI', 'Finalizado'

    unit = models.ForeignKey(
        Unit,
        related_name='products',
        on_delete=models.CASCADE
    )
    technician = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='maintenances'
    )
    tag = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
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
            models.Index(fields=['unit', 'technician']),
            models.Index(fields=['created']),
        ]
        verbose_name = 'manutenção'
        verbose_name_plural = 'manutenções'

    def__str__(self):
        return self.name