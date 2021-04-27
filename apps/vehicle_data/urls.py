
from django.urls import path

from .views import VehicleInformationAPI,PendingVehicleAPI,VehicleCompletionAPI

app_name='vehicle_data'

urlpatterns= [
    path('vehicle-ap/', VehicleInformationAPI.as_view()),

    path('vehicle-ap/pending', PendingVehicleAPI.as_view()),
    path('vehicle-ap/complete', VehicleCompletionAPI.as_view()),
]

