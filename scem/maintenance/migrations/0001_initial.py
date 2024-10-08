# Generated by Django 5.1.1 on 2024-10-04 21:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Unit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                (
                    "manager",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="manager",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "order",
                "verbose_name_plural": "unities",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("requestor", models.CharField(max_length=200)),
                ("addr", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=200)),
                ("tag", models.CharField(blank=True, max_length=200, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("start_time", models.TimeField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                ("end_time", models.TimeField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("EF", "Em fila"),
                            ("EA", "Em atendimento"),
                            ("FI", "Finalizado"),
                        ],
                        default="EF",
                        max_length=2,
                    ),
                ),
                ("slug", models.SlugField(max_length=200)),
                (
                    "technician",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="maintenance.unit",
                    ),
                ),
            ],
            options={
                "verbose_name": "order",
                "verbose_name_plural": "orders",
                "ordering": ["created"],
            },
        ),
        migrations.AddIndex(
            model_name="unit",
            index=models.Index(fields=["name"], name="maintenance_name_001a85_idx"),
        ),
        migrations.AddIndex(
            model_name="order",
            index=models.Index(fields=["id", "slug"], name="maintenance_id_3dcc34_idx"),
        ),
        migrations.AddIndex(
            model_name="order",
            index=models.Index(
                fields=["technician"], name="maintenance_technic_d1a881_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="order",
            index=models.Index(
                fields=["created"], name="maintenance_created_7e4ca5_idx"
            ),
        ),
    ]
