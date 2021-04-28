from django.db import models
from authentication.models import  User
# Create your models here.

class ClientInformation(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mothers_last_name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=1000)
    age = models.IntegerField()
    email =models.EmailField(max_length = 500)
    phone =models.CharField(max_length=30,blank=True,null=True)

    street = models.CharField(max_length=1000)
    internal_number = models.IntegerField()
    external_number = models.IntegerField()
    cologne = models.CharField(max_length=1000)
    delegation_municipality = models.CharField(max_length=1000)
    town = models.CharField(max_length=1000)
    rfc = models.CharField(max_length=1000)
    joindate = models.DateTimeField(auto_now_add=True)
    served_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='client_user')

    def __str__(self):
            return self.first_name
    class Meta:
        ordering = ('-id',)
    @classmethod
    def create_client(cls,data):
        """
            Create and return a CLIENT.
        """
        print('fromcrcecercercec')

        print(data)
        result = cls.objects.create(
            first_name=data['first_name'],
            second_name=data['second_name'],
            last_name = data['last_name'],
            mothers_last_name =data['mothers_last_name'],
            nationality = data['nationality'],
            age=data['age'],
            email=data['email'],
            phone = data['phone'],
            street = data['street'],
            internal_number = data['internal_number'] , 
            external_number = data['external_number'] ,
            cologne = data['cologne'],
            delegation_municipality = data['delegation_municipality'],
            town =data['town'],
            rfc =data ['rfc'],
            served_by=data['user']
            )
        result.save()
        print(result)
        return result
    @classmethod
    def get_all(cls):
        """
        get all clients
        """
        all_clients = cls.objects.all().order_by('-id')

        return all_clients

