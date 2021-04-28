from django.shortcuts import render

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# from .serializers import RegistrationSerializer


from django.http import JsonResponse

from .serializers import  ReviewSerializerView

class NewReviewAPI(APIView): #FOR CALCULATING THE AVERAGE QUALIFICATION FOR EVERYTECHNICIAN FROM THE REVIEWS FIRST QUESTION
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializerView
    def post(self,request):
        print(request.data)
        data = request.data

        serializer=self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            
       

        return Response(serializer,status=status.HTTP_400_BAD_REQUEST)
    
