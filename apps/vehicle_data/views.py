from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import VehicleInformationSerializer

from .models import ClientInformation,VehicleData

from .cust_date import  filtDate
import pytz
from django.conf import settings
from datetime import date,datetime,timedelta

# Create your views here.

class VehicleInformationAPI(APIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = VehicleInformationSerializer
    def get(self,request):
        all_clients = ClientInformation.get_all()
        serializer =self.serializer_class(all_clients,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        print(request.data['data'])
        data = request.data['data']
        data['technician_incharge']=request.user.id

        serializer=self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            
       

        return Response(serializer,status=status.HTTP_400_BAD_REQUEST)





class PendingVehicleAPI(APIView):   #TO GET ALL PENDING VEHICLE and filter by the currentuser during departure of vehicle
    permission_classes = (IsAuthenticated,)

    serializer_class = VehicleInformationSerializer
    def get(self,request):
        current_userid=request.user.id
        
        all_pending_vehicles = VehicleData.get_by_status_and_currentuser(current_userid,'pending')
        serializer =self.serializer_class(all_pending_vehicles,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

class VehicleCompletionAPI(APIView):  #TO UPDATE ON COMPLETION OF VEHICLE
    permission_classes = (IsAuthenticated,)

    serializer_class = VehicleInformationSerializer
    def post(self,request):
        
        try:
        
            vehicleid = request.data['vehicle']
            vehicle = VehicleData.objects.filter(id=vehicleid).update(
                status=request.data['status'],
                liters_of_gasoline_on_departure =request.data['liters_of_gasoline_on_departure'],
                actual_service_performed=request.data['actual_service_performed'],
                actual_delivery_date=datetime.now().replace(tzinfo=pytz.timezone(settings.TIME_ZONE)),
                vehicle_observation_on_departure=request.data['vehicle_observation_on_departure']
                )
            serializer=self.serializer_class(vehicle)
            return Response({'message':'Successful'},status=status.HTTP_201_CREATED)
        except :
            return Response(status=status.HTTP_400_BAD_REQUEST)
