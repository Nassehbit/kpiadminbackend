
from django.urls import path

from .views import clientInformationAPI

app_name='authentication'

urlpatterns= [
    path('client-ap/', clientInformationAPI.as_view()),
]

