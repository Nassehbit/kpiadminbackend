
from django.urls import path

from .views import NewReviewAPI 

app_name='client'

urlpatterns= [
  
     path('newreview/',NewReviewAPI.as_view()), 
  
]

