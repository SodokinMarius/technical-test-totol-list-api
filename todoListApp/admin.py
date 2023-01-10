from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import Task
@admin.register(Task)
class UserAdmin(DefaultUserAdmin):
    list_display=('title','description','progress_status')
    