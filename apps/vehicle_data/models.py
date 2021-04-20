from django.db import models
from authentication.models import  User
from apps.client.models import  ClientInformation
# Create your models here.

class VehicleData(models.Model): 
    vehicle_plate = models.CharField(max_length=200,unique=True)
    vehicle_brand = models.CharField(max_length=200,unique=True)
    vehicle_model = models.CharField(max_length=200,unique=True)
    vehicle_year  = models.IntegerField()
    vehicle_color = models.CharField(max_length=1000,unique=True)
    vehicle_observation = models.IntegerField()
    vehicle_entry_date = models.IntegerField()
    liters_of_gasoline = models.CharField(max_length=1000,unique=True)
    solicited_service = models.CharField(max_length=1000,unique=True)
    service_specification = models.CharField(max_length=1000,unique=True)
    proposed_departure_date = models.IntegerField()
    client_id = models.ForeignKey(ClientInformation,on_delete=models.CASCADE,null=True,related_name='client_id')
    technician_incharge = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='user_client')

    def __str__(self):
        return self.vehicle_plate
    class Meta:
        ordering = ('-id',)