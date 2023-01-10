from django.urls import path,include
from rest_framework import routers

from .viewsets import *


router = routers.SimpleRouter()

router.register('tasks',TaskViewSet,basename='tasks')


urlpatterns = router.urls  