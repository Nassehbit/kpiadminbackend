
from django.urls import path

from .views import VehicleInformationAPI

app_name='authentication'

urlpatterns= [
    path('vehicle-ap/', VehicleInformationAPI.as_view()),
    

]

