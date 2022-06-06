from django.contrib import admin
from .models import student,person,image
# Register your models here.
@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'semester']

@admin.register(person)
class PersonAdmin(admin.ModelAdmin):
    list_display= ('first_name', 'last_name', 'date')

@admin.register(image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image_title','image_cat','image_pub_date', 'user']