from .renderers import UserJSONRenderer,PROFILEJSONRenderer
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .exceptions import ProfileDoesNotExist
from .serializers import(
     RegistrationSerializer,LoginSerializer,UserSerializer,
     ProfileSerializer,AllRolesSerializer,Userseriliz,AllTechnicianSerializer)

from .models import Profile,Roles,User
from django.http import JsonResponse

# Create your views here.

class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    renderer_classes=(UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        print(user)
        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't  have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        print("1111Fvsdcsdc")
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        print("Fvsdcsdc")
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        # There is nothing to validate or save here. Instead, we just want the
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
        user_data = request.data.get('user', {})

        serializer_data = {
            'username': user_data.get('username', request.user.username),
            'email': user_data.get('email', request.user.email),

            'profile': {
                'bio': user_data.get('bio', request.user.profile.bio),
                'image': user_data.get('image', request.user.profile.image)
                }
            }
        # Here is that serialize, validate, save pattern we talked about
        # before.
        serializer = self.serializer_class(request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class ProfileRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    # renderer_classes = (PROFILEJSONRenderer)
    serializer_class = ProfileSerializer

    def retrieve(self, request, username, *args, **kwargs):
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        try:
            # We use the `select_related` method to avoid making unnecessary
            # database calls.
            profile = Profile.objects.select_related('user').get( user__username=username)
        except Profile.DoesNotExist:
            raise ProfileDoesNotExist

        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)

class AllRolesview(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AllRolesSerializer

    def get(self, request):
        try:
            roles = Roles.objects.all()
        except:
            return Response({"message":"No data found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(roles,many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class AllTechnicianAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AllTechnicianSerializer

    def get(self, request):
        try:
            roles = User.objects.filter(role_id=2).all()
        except:
            return Response({"message":"No data found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(roles,many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class TechnicianDeliveryAPI(APIView): #FOR CALCULATING THE ONTIME AND OUT OF TIME DELIVERY SERVICES
    permission_classes = (IsAuthenticated,)
    serializer_class = Userseriliz

    def get(self, request):
        current_userid=request.user.id
        print(current_userid)
        finalobject=[]
        all_users = User.objects.filter(role_id=2).all()
        
        for user in all_users:
            
            vehicles = User.objects.get(id=user.id).user_client.filter(status='completed').all()
            counter = {'services_on_Time':0,'services_out_of_time':0}
            for vehicle in vehicles:
                
                if vehicle.proposed_departure_date < vehicle.actual_delivery_date:
                    print('late!!!!!')
                    counter['services_out_of_time']+=1
                else:
                    # print(counter.services_on_Time)
                    counter['services_on_Time']+=1
                    print('huraaay!@')
                print (vehicle.status)
            print(counter)
            user_obj ={user.username:counter} 
            finalobject.append(user_obj)
      
            print('****************************************')
            
            print(vehicles)
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^666666')
        print(finalobject)
        # serializer = self.serializer_class(vehicles)
        return JsonResponse({'data':finalobject},status=status.HTTP_200_OK)

        # return Response(serializer.data, status=status.HTTP_200_OK)


class TechnicianReviewAverageAPI(APIView): #FOR CALCULATING THE AVERAGE QUALIFICATION FOR EVERYTECHNICIAN FROM THE REVIEWS FIRST QUESTION
    permission_classes = (IsAuthenticated,)
    serializer_class = Userseriliz

    def get(self, request):
        current_userid=request.user.id
        print(current_userid)
        finalobject=[]
        all_users = User.objects.filter(role_id=2).all()
        
        for user in all_users:
            
            all_reviews = User.objects.get(id=user.id).user_review.all()
            # counter = {'services_on_Time':0,'services_out_of_time':0}
            print()
            total_reviews = len(all_reviews) * 10
            received_reviews =0
            for review in all_reviews:
                received_reviews+=float(review.technicians_attention)
              
                # print (review)
            try:
                average_rating =(received_reviews *100)/total_reviews
            except ZeroDivisionError:
                average_rating =0

            user_obj =[user.username,average_rating]
            finalobject.append(user_obj)
      
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^666666')
        print(finalobject)
        # serializer = self.serializer_class(vehicles)
        return JsonResponse({'data':finalobject},status=status.HTTP_200_OK)

        # return Response(serializer.data, status=status.HTTP_200_OK)



class TechnicianAverageGasolineAPI(APIView): 
    """
    Compare Liters of Gasoline in Tank from "Technician Form 1" with Liters of Gasoline Left from "Technician Form 2"
    and calculate the fuel  average that a technician use per service (in a week)
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = Userseriliz

    def get(self, request):
        current_userid=request.user.id
        print(current_userid)
        finalobject=[]
        all_users = User.objects.filter(role_id=2).all()
        
        for user in all_users:
            
            vehicles = User.objects.get(id=user.id).user_client.filter(status='completed').all()
            initial_total_amount_of_gasoline = 0
            final_amount_of_gasoline = 0
            for vehicle in vehicles:
               initial_total_amount_of_gasoline +=float(vehicle.liters_of_gasoline_on_arrival)
               final_amount_of_gasoline +=float(vehicle.liters_of_gasoline_on_departure)
            try:
                average_usage_of_gasoline=100 - ((final_amount_of_gasoline*100)/initial_total_amount_of_gasoline)
            except ZeroDivisionError:
                average_usage_of_gasoline =0
            
            user_obj =[user.username,average_usage_of_gasoline]
            finalobject.append(user_obj)
      
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^666666')
        print(finalobject)
        # serializer = self.serializer_class(vehicles)
        return JsonResponse({'data':finalobject},status=status.HTTP_200_OK)

        # return Response(serializer.data, status=status.HTTP_200_OK)