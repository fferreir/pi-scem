# Generated by Django 5.1.1 on 2024-10-24 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maintenance", "0002_alter_order_options_alter_unit_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[("EF", "Em fila"), ("FI", "Finalizado")],
                default="EF",
                max_length=2,
            ),
        ),
    ]
