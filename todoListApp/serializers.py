from rest_framework import serializers
from .models import Task

from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description','date_start' 'date_end','progress_status' 'is_cancelled']
        read_only_fields = ['progress_status','is_cancelled','user','created_at']
        
      