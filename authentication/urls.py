from django.urls import path

from .views import RegistrationAPIView,LoginAPIView,UserRetrieveUpdateAPIView,ProfileRetrieveAPIView,AllRolesview

app_name='authentication'

urlpatterns= [
    path('user', UserRetrieveUpdateAPIView.as_view()),
    path('users/',RegistrationAPIView.as_view()),
    path('login/',LoginAPIView.as_view()),
    path('profiles/<str:username>', ProfileRetrieveAPIView.as_view()),
     path('roles/',AllRolesview.as_view()),
]