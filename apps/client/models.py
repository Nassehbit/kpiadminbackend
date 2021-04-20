from django.db import models
from authentication.models import  User
# Create your models here.

class ClientInformation(models.Model):
    first_name = models.CharField(max_length=200,unique=True)
    second_name = models.CharField(max_length=200,unique=True)
    last_name = models.CharField(max_length=200,unique=True)
    mothers_last_name = models.CharField(max_length=200,unique=True)
    street = models.CharField(max_length=1000,unique=True)
    internal_number = models.IntegerField()
    external_number = models.IntegerField()
    cologne = models.CharField(max_length=1000,unique=True)
    delegation_municipality = models.CharField(max_length=1000,unique=True)
    town = models.CharField(max_length=1000,unique=True)
    age = models.IntegerField()
    phone =models.IntegerField()
    rfc = models.CharField(max_length=1000,unique=True)
    email =models.EmailField(max_length = 500)
    nationality = models.CharField(max_length=1000,unique=True)
    served_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='client_user')

    def __str__(self):
            return self.first_name
    class Meta:
        ordering = ('-id',)
