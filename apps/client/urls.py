
from django.urls import path

from .views import clientInformationAPI,ClientDataFilterAPI 

app_name='client'

urlpatterns= [
    path('client-ap/', clientInformationAPI.as_view()),
    path('client-ap/date-filtered/', ClientDataFilterAPI.as_view()),
]

