from django.contrib import admin
from .models import person,image

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display= ('first_name', 'last_name')


class ImageAdmin(admin.ModelAdmin):
    list_display = ['image_title','image_cat','image_pub_date', 'user']


admin.site.register(person,PersonAdmin)
admin.site.register(image,ImageAdmin)

