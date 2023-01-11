from rest_framework import serializers
from .models import Task

from .models import *
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'date_start', 'date_end', 'progress_status', 'is_cancelled', 'user', 'created_at')
        read_only_fields = ('progress_status', 'is_cancelled', 'user', 'created_at',)
    
    def create(self, validated_data):
        # remove isValid field from validated_data
        validated_data.pop('isValid', None)
        return Task.objects.create(**validated_data)