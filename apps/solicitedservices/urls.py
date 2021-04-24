
from django.urls import path

# from .views import clientInformationAPI,ClientDataFilterAPI 
from .views import  SolicitedServiceAPI,SolicitedVehicleFilteredAPI
app_name='solicitedservices'

urlpatterns= [
    path('solicited-ap/', SolicitedServiceAPI.as_view()),
     path('solicited-ap/filtered', SolicitedVehicleFilteredAPI.as_view()),

    # path('client-ap/date-filtered/', ClientDataFilterAPI.as_view()),

]

