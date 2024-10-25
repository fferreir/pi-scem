# Generated by Django 5.1.1 on 2024-10-23 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maintenance", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={
                "ordering": ["created"],
                "verbose_name": "ordem",
                "verbose_name_plural": "ordens",
            },
        ),
        migrations.AlterModelOptions(
            name="unit",
            options={
                "ordering": ["name"],
                "verbose_name": "unidade",
                "verbose_name_plural": "unidades",
            },
        ),
        migrations.AddField(
            model_name="order",
            name="normal_time",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="over_time",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]