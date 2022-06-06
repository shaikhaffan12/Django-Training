from django.db import models

# Create your models here.

class person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

class image(models.Model):
    user = models.ForeignKey(person, on_delete= models.CASCADE)
    image_title = models.CharField(max_length=40)
    image_cat = models.CharField(max_length=40)
    image_pub_date = models.DateField()

