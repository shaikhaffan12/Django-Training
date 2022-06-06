from django.contrib import admin
from .models import person,song
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']

class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name', 'song_cat', 'song_pub_date', 'written_by']

admin.site.register(person, PersonAdmin)
admin.site.register(song, SongAdmin)