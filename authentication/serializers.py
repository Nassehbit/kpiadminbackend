from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User,Profile,Roles
from apps.vehicle_data.serializers import VehicleInformationSerializer
class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)
    # role=serializers.CharField(source="Roles.name")
    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['email', 'username', 'role','password', 'token']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        return User.objects.create_user(**validated_data)


##LOGIN SERIALIZER
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    # role=serializers.CharField(source="roles.id",read_only=True)
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    bio = serializers.CharField(allow_blank=True, required=False)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('username', 'bio', 'image',)
        read_only_fields = ('username',)

    def get_image(self, obj):
        if obj.image:
            return obj.image

        return 'https://static.productionready.io/images/smiley-cyrus.jpg'
#####update of a token
class UserSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""


    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

   
    profile = ProfileSerializer(write_only=True)
    bio = serializers.CharField(source='profile.bio', read_only=True)
    image = serializers.CharField(source='profile.image', read_only=True)
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token','profile', 'bio','image')
        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        """Performs an update on a User."""

        password = validated_data.pop('password', None)

       
        profile_data = validated_data.pop('profile', {})

        for (key, value) in validated_data.items():
       
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)
        instance.save()
        for (key, value) in profile_data.items():
            setattr(instance.profile, key, value)

        instance.profile.save()
        return instance


#####update of a token
class  AllRolesSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    class Meta:
            model = Roles
            fields='__all__'

class  Userseriliz(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""
    # email = serializers.CharField(max_length=255)
    # username = serializers.CharField(max_length=255, read_only=True)
    # password = serializers.CharField(max_length=128, write_only=True)
    user_client =VehicleInformationSerializer (many=True,read_only=True)
    # token = serializers.CharField(max_length=255, read_only=True)
    class Meta:
            model = User
            fields=['user_client']