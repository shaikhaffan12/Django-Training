from django.db import models
from django.utils import timezone

# Create your models here.
class student(models.Model):
    sem_choices = (
        ('1','1'),
        ('2','2')
    )
    name = models.CharField(max_length=40)
    roll = models.IntegerField()
    city = models.CharField(max_length=20)
    semester = models.CharField(max_length=10,choices=sem_choices, default='1')


class person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=timezone.now)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

class image(models.Model):
    user = models.ForeignKey(person, on_delete= models.CASCADE)
    image_title = models.CharField(max_length=40)
    image_cat = models.CharField(max_length=40)
    image_pub_date = models.DateField()