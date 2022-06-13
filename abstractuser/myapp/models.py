from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    username = models.CharField(max_length=20,blank=True,null=True,unique=True)
    name = models.CharField(max_length=50,blank=False,null=False)
    email = models.EmailField(('email address'),unique=True)
    phone_no = models.CharField(max_length=13,blank=True,null=True)

    USERNAME_FIELD =  'email'
    REQUIRED_FIELDS =  ['username','first_name']

    def __str__(self):
        return self.email