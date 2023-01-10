from djoser.serializers import UserCreateSerializer

from .models import User 
from rest_framework import serializers

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['username','email','full_name','address','phone'] 
        extra_kwargs = {'password': {'write_only': True}}
        depth = 1