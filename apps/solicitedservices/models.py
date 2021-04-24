from django.db import models

# Create your models here.
from django.db import models
from authentication.models import  User
# Create your models here.

class SolicitedService(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
            return self.name
    class Meta:
        ordering = ('id',)
    @classmethod
    def get_all(cls):
        """
        get all clients
        """
        all_services = cls.objects.all().order_by('-id')

        return all_services

    @classmethod
    def filter_by_vehicle_entry_date(cls,start_date,end_date):
        """"
        to
        """
        filtered_data =cls.objects.filter(solicited_Vehicles__vehicle_entry_date__gte=start_date,solicited_Vehicles__vehicle_entry_date__lte=end_date).all().distinct()
        return filtered_data