from djoser.serializers import UserCreatePasswordRetypeSerializer

from .models import User 
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
   
 
