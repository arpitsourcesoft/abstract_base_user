from enum import unique
from pickle import TRUE
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

class User(AbstractBaseUser):

    username =  models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=TRUE)
    mobile = models.CharField(max_length=14)
    is_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    forget_password = models.CharField(max_length=100, null=True, blank=True)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_logout_time = models.DateTimeField(null=True, blank=True)


    objects = UserManager()


    USERNAME_FIELD = 'email'

    REQUIRED_FIELD = ['username']
    



