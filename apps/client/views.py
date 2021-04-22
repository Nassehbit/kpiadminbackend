from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ClientInformationSerializer

from .models import ClientInformation

# Create your views here.

class clientInformationAPI(APIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = ClientInformationSerializer
    def get(self,request):
        all_clients = ClientInformation.get_all()
        serializer =self.serializer_class(all_clients,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        print(request.data['data'])
        data = request.data['data']
        data['served_by']=request.user.id
        # res = ClientInformation.create_client(data)
        # serializer = self.serializer_class(data=res)

        serializer=self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            
       

        return Response(status=status.HTTP_400_BAD_REQUEST)