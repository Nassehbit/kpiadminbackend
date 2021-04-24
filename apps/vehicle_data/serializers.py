from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import VehicleData


class BaseVehicleInformationSerializer(serializers.ModelSerializer):
    """
    ***THIS IS THE BASE SERIALIZER
    iNHERIT FROM THIS
    """
    solicited_service_name=serializers.CharField(source='solicited_service.name',read_only=True)
    class Meta:
        model = VehicleData

        fields='__all__'


class VehicleInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleData

        fields='__all__'
