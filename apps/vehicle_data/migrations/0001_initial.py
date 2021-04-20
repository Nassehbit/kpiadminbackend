# Generated by Django 3.2 on 2021-04-20 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_plate', models.CharField(max_length=200, unique=True)),
                ('vehicle_brand', models.CharField(max_length=200, unique=True)),
                ('vehicle_model', models.CharField(max_length=200, unique=True)),
                ('vehicle_year', models.IntegerField()),
                ('vehicle_color', models.CharField(max_length=1000, unique=True)),
                ('vehicle_observation', models.IntegerField()),
                ('vehicle_entry_date', models.IntegerField()),
                ('liters_of_gasoline', models.CharField(max_length=1000, unique=True)),
                ('solicited_service', models.CharField(max_length=1000, unique=True)),
                ('service_specification', models.CharField(max_length=1000, unique=True)),
                ('proposed_departure_date', models.IntegerField()),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_id', to='client.clientinformation')),
                ('technician_incharge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
