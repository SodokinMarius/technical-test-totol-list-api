from django.contrib import admin
from django.urls import path,include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


#-----------------------------------------------------#
#                   SWAGGER CONFIGURATION             #
#-----------------------------------------------------#
schema_view = get_schema_view(
   openapi.Info(
      title="TODO LIST API",
      default_version='v1',
      description="API for tasks managing",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


from django.contrib import admin
from django.urls import path,include 

urlpatterns = [
    path('admin/', admin.site.urls),
    
       
#-----------------------------------------------------#
#                   SWAGGER ROUTER                    #
#-----------------------------------------------------#
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
#-----------------------------------------------------#
#                   AUTHENTICATION ROUTER             #
#-----------------------------------------------------#
    path('auth/', include('authentication.urls')),
    
    
#-----------------------------------------------------#
#                  TODO   ROUTER           #
#-----------------------------------------------------#
    path('todo-list/', include('todoListApp.urls')),
]
