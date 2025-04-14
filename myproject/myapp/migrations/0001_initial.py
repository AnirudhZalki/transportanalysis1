# Generated by Django 5.2 on 2025-04-08 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VehicleTrip",
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
                ("source", models.CharField(max_length=100)),
                ("destination", models.CharField(max_length=100)),
                ("distance", models.FloatField()),
                ("tolls", models.IntegerField()),
                ("fuel_cost", models.FloatField()),
                ("toll_charges", models.FloatField()),
                ("total", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
