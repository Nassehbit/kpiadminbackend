from django.db import models
from authentication.models import  User
from apps.client.models import  ClientInformation
from apps.solicitedservices.models import  SolicitedService
# Create your models here.

class VehicleData(models.Model): 
    vehicle_plate = models.CharField(max_length=200)
    vehicle_brand = models.CharField(max_length=200)
    vehicle_model = models.CharField(max_length=200)
    vehicle_year  = models.IntegerField()
    vehicle_color = models.CharField(max_length=1000)
    vehicle_observation = models.IntegerField() #######
    vehicle_entry_date = models.DateTimeField( auto_now=False, auto_now_add=False)
    liters_of_gasoline = models.CharField(max_length=1000) #######
    
    
    service_specification = models.CharField(max_length=1000)
    proposed_departure_date = models.DateTimeField( auto_now=False, auto_now_add=False)

    solicited_service = models.ForeignKey(SolicitedService,on_delete=models.CASCADE,related_name='solicited_Vehicles')
    client_id = models.ForeignKey(ClientInformation,on_delete=models.CASCADE,null=True,related_name='client_id')
    technician_incharge = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='user_client')

    def __str__(self):
        return self.vehicle_plate
    class Meta:
        ordering = ('-id',)
    @classmethod
    def get_all(cls):
        """
        get all clients
        """
        all_vehicle = cls.objects.all().order_by('id')

        return all_vehicle

    @classmethod
    def filter_by_vehicle_entry_date(cls,start_date,end_date):
        """"
        to
        """
        filtered_data =cls.objects.filter(vehicle_entry_date__gte=start_date,vehicle_entry_date__lte=end_date)

        return filtered_data