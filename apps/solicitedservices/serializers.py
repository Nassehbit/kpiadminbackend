from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import SolicitedService
from apps.vehicle_data.serializers import  BaseVehicleInformationSerializer
from rest_framework.fields import SerializerMethodField
from django.core.serializers import json
class BaseSolicitedServiceSerializer(serializers.ModelSerializer):
    """
    THIS DOESNT BACKREF TABLES REFERECING IT
    The base class 
    """
    class Meta:
        model=SolicitedService
        fields='__all__'
class SolicitedVehicleFilteredSerializer(BaseVehicleInformationSerializer):
    """
    THIS BACKREFS TABLES REFERECING IT FROM VEHICLE APP
    """
    # solicited_Vehicles= SerializerMethodField()
    # def get_solicited_Vehicles(self, obj):
    #     print(obj)
    #     print(obj)
    #     return obj
    # class Meta
    #     model=SubCategory
    #     fields='__all__'

class SolicitedServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = SolicitedService

        fields='__all__'
