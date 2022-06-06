from django.db import models

# Create your models here.
class person(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

class song(models.Model):
    Person = models.ManyToManyField(person)
    song_name = models.CharField(max_length=50)
    song_cat = models.CharField(max_length=40)
    song_pub_date = models.DateField()

    def written_by (self):
        return ",".join([str(p) for p in self.Person.all()])
