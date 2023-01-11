"""from djoser.serializers import UserCreatePasswordRetypeSerializer

from rest_framework import serializers

class UserCreateSerializer(UserCreatePasswordRetypeSerializer):
    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        model = User
        fields = ['username','full_name','password'] 
        read_only_fields =('date_joined',)
        
        extra_kwargs = {
            'password': {'write_only': True}
            }
        depth = 1
   
 
"""
from .models import User 

from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ['username', 'full_name', 'password']
        read_only_fields = ('date_joined',)
        extra_kwargs = {
            'password': {'write_only': True}
        }