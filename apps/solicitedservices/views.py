from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SolicitedServiceSerializer,SolicitedVehicleFilteredSerializer

from .models import SolicitedService
from apps.vehicle_data.models import VehicleData
from apps.vehicle_data.cust_date import  filtDate
from django.core.serializers import json
# Create your views here.

class SolicitedServiceAPI(APIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = SolicitedServiceSerializer
    def get(self,request):
        all_clients = SolicitedService.get_all()
        serializer =self.serializer_class(all_clients,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)


class SolicitedVehicleFilteredAPI(APIView):
    """
    FILTERED TO THE VEHICLES REFERENCING CERTAIN SERVICES
    """
    permission_classes = (IsAuthenticated,)

    serializer_class = SolicitedVehicleFilteredSerializer
    def get(self,request):
        time_result = filtDate()
        print(time_result['first'])
        print(time_result['today'])
        filt = VehicleData.filter_by_vehicle_entry_date(time_result['first'],time_result['today'])
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print(filt)

        # filtered_data = VehicleData.filter_by_vehicle_entry_date(time_result['first'],time_result['today'])
        # print(filtered_data)
     
        serializer =self.serializer_class(filt,many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)