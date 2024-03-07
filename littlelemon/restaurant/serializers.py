from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import *


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ("id", "title", "price", "inventory")


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]
        # extra_kwargs = {"password": {"write_only": True}}
