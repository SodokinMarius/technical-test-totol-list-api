from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *

from rest_framework import permissions

from .permissions import isOwnerOrReadOnly
from .models import *


from django.db.models.functions import Now

import datetime 

from .enums import  ProgressChoiceEnum

class TaskViewSet(viewsets.ModelViewSet):    
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
     #return the permission depende by the action that the user want to perform
    def get_permissions(self):
        action = self.action
        if action =='create':
           return [permissions.IsAuthenticated()]
        elif  action in ('update', 'partial_update',):      
            return [permissions.IsAdminUser(),permissions.IsAuthenticated()]
        else :
            return [isOwnerOrReadOnly(),permissions.IsAuthenticated()] 
  
  
    def perform_create(self, serializer):
        if serializer.is_valid():     
            serializer.save(user=self.request.user,isValid=True,progress_status=ProgressChoiceEnum.Pending.value)
            return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(data={'message':'Invalid provided data'},status=status.HTTP_400_BAD_REQUEST)

    # return challenges list for the owned by the connected user
    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = self.queryset.filter(user=user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)

        if self.action == 'get_recent_tasks':
             queryset = queryset.order_by("-created_at")[:20]

        return queryset
    
   
    def perform_destroy(self, instance):
        if (instance.user == self.request.user) and instance.progress_status == ProgressChoiceEnum.Pending.value:
            instance.delete()
            return Response(data={"message":"Deleted succesfully !"},status=status.HTTP_202_ACCEPTED)
        return Response(data={"message":"You must be owner or admin and the challenge must be in pending"},status=status.HTTP_401_UNAUTHORIZED)


    def perform_update(self, serializer):
        user = serializer.validated_data['user']
        if (user == self.request.user ) and serializer.validated_data['progress_status'] == ProgressChoiceEnum.Pending.value:
            serializer.save()
            return Response(data={"message":"Updated succesfully !"},status=status.HTTP_202_ACCEPTED)
        return Response(data={"message":"You must be owner or admin and the challenge must be in pending"},status=status.HTTP_401_UNAUTHORIZED)
    
    @action(methods=['get'],detail=False,url_path = "recent",url_name ="recent")
    def get_recent_tasks(self,request):
        queryset = self.filter_queryset(self.get_queryset())[:20]
        serializer = TaskSerializer(queryset,many=True)
        return Response(data=serializer.data,status= status.HTTP_200_OK)
    
    
    @action(methods=['get'],detail=False,url_path = "in_progress",url_name ="in_progress")
    def get_inprogress_tasks(self,request):
        queryset = Task.objects.filter(progress_status=ProgressChoiceEnum.InProgress.value)
        serializer = TaskSerializer(queryset,many=True)
        return Response(data=serializer.data,status= status.HTTP_200_OK)
    
    @action(methods=['get'],detail=False,url_path = "delayed",url_name ="delayed")
    def get_inprogress_tasks(self,request):
        queryset = Task.objects.filter(progress_status=ProgressChoiceEnum.Delayed.value)
        serializer = TaskSerializer(queryset,many=True)
        return Response(data=serializer.data,status= status.HTTP_200_OK)

    @action(methods=['get'],detail=False,url_path = "pending",url_name ="pending")
    def get_pending_tasks(self,request):
        queryset = Task.objects.filter(progress_status=ProgressChoiceEnum.Pending.value)
        serializer = TaskSerializer(queryset,many=True)
        return Response(data=serializer.data,status= status.HTTP_200_OK)
    
    @action(methods=['get'],detail=False,url_path = "completed",url_name ="completed")
    def get_pending_tasks(self,request):
        queryset = Task.objects.filter(progress_status=ProgressChoiceEnum.Completed.value)
        serializer = TaskSerializer(queryset,many=True)
        return Response(data=serializer.data,status= status.HTTP_200_OK)