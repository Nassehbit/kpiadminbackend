
from django.urls import path

from .views import VehicleInformationAPI

app_name='vehicle_data'

urlpatterns= [
    path('vehicle-ap/', VehicleInformationAPI.as_view()),
    

]

