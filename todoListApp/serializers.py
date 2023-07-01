from rest_framework import serializers
from .models import Task

from .models import *
class TaskSerializer(serializers.ModelSerializer):
    file = serializers.FileField(allow_null=True,required=True)
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'date_start', 'date_end', 'progress_status', 'is_cancelled', 'user', 'created_at','file')
        read_only_fields = ('progress_status', 'is_cancelled', 'user', 'created_at',)

    def create(self, validated_data):
        # remove isValid field from validated_data
        validated_data.pop('isValid', None)
        file = validated_data.pop('file')
        print("Fichier",file.name)
        task = Task.objects.create(**validated_data)
        task.file = file
        task.save()
        return task