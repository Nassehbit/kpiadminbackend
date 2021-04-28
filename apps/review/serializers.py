
from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import Review

class  ReviewSerializerView(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    class Meta:
            model = Review
            fields='__all__'