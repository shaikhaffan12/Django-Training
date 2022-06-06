from pyexpat import model
from django.db import models

# Create your models here.
class student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    roll_no = models.IntegerField()