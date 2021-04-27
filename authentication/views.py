from .renderers import UserJSONRenderer,PROFILEJSONRenderer
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView,RetrieveAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .exceptions import ProfileDoesNotExist
from .serializers import RegistrationSerializer,LoginSerializer,UserSerializer,ProfileSerializer,AllRolesSerializer,Userseriliz

from .models import Profile,Roles,User

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


class TechnicianDeliveryAPI(APIView): #FOR CALCULATING THE ONTIME AND OUT OF TIME DELIVERY SERVICES
    permission_classes = (IsAuthenticated,)
    serializer_class = Userseriliz

    def get(self, request):
        current_userid=request.user.id
        print(current_userid)
        # try:
        #     vehicles = User.objects.filter(id=current_userid).all()
        #     print('****************************************')
        #     print(vehicles)
        #     serializer = self.serializer_class(vehicles)
        #     return Response(serializer.dat,status=status.HTTP_200_OK)
        # except:
        #     return Response({"message":"No data found"}, status=status.HTTP_404_NOT_FOUND)

        vehicles = User.objects.get(id=current_userid)
        print('****************************************')
        print(vehicles)
        serializer = self.serializer_class(vehicles)
        return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(serializer.data, status=status.HTTP_200_OK)