from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    
)
from .validators import(
     usernameValidator,  
     passwordValidator
)

class UserManager(BaseUserManager):
    def create_user(self,username ,password=None,**extra_fields):
        if not username:
            raise ValueError("User must have an username")
        
        user = self.model(
            username = self.normalize_username(username),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,password,**kwargs):
        if not username:
            raise ValueError("User must have a username")
        
        user = self.create_user(
            username= self.normalize_username(username),
            password= password,
            **kwargs
        )
        
        user.is_admin = True
        user.is_staff = True
        user.is_superuser =  True 
        user.save(using=self._db)
        return user 

class User(AbstractBaseUser):
    username = models.CharField(verbose_name="Username",max_length=250,validators=usernameValidator())
    password = models.CharField(verbose_name="Password",validators=passwordValidator())
    full_name = models.CharField(verbose_name="Complete Name",max_length=250)
    profile_photo = models.ImageField(upload_to="users",verbose_name="Photo de profil",null=True)
    is_valid = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_verified =  models.BooleanField(default=True)
    is_staff =   models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager() 
    
    USERNAME_FIELD = 'username'
    
    
    def __str__(self) -> str:
         return  self.username
     
    def has_perm(self, perm, obj=None):
            return self.is_admin
