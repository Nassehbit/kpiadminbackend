from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import VehicleData

class VehicleInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleData

        fields='__all__'
