from django.contrib import admin
from Service.models import ServiceUser
from Service.models import Song
from Service.models import SharedSong


class User(admin.ModelAdmin):
    list_display = ('userId', 'name', 'username', 'gender', 'password')


admin.site.register(ServiceUser, User)


class Songs(admin.ModelAdmin):
    list_display = ('songId', 'title', 'singer_name', 'song',
                    'songs_image', 'privacy', 'users_email')


admin.site.register(Song, Songs)


class Sharedsongs(admin.ModelAdmin):
    list_display = ('shareId', 'email', 'singer_name',
                    'songName', 'song', 'songs_image', 'songName', 'sharedBy')


admin.site.register(SharedSong, Sharedsongs)

# Register your models here.
