from django.db import models
from authentication.models import  User
from apps.client.models import  ClientInformation
from apps.solicitedservices.models import  SolicitedService
# Create your models here.

class Review(models.Model): 
   
    technicians_attention = models.CharField(max_length=200)
    level_of_satisfaction = models.CharField(max_length=200)
    request_services_again = models.CharField(max_length=200) #would_they_request_for_services_again
    reccomend_to_others = models.CharField(max_length=200) #would_they_recommend our services
    comments = models.CharField(max_length=1000)
    technician_incharge = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='user_review')

    def __str__(self):
        return self.technician_incharge
    class Meta:
        ordering = ('-id',)
    @classmethod
    def get_all(cls):
        """
        get all reviews
        """
        all_reviews = cls.objects.all().order_by('id')

        return all_reviews
 