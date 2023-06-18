from django.db import models


class ServiceUser(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=15)


class Song(models.Model):

    songId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    singer_name = models.CharField(max_length=250)
    song = models.FileField(
        upload_to="songs/", max_length=250, null=True, default=None)
    songs_image = models.FileField(
        upload_to="song-photo/", max_length=250, null=True, default=None)
    privacy = models.CharField(max_length=15)
    users_email = models.CharField(max_length=250)


class SharedSong(models.Model):
    shareId = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    singer_name = models.CharField(max_length=250)
    songName = models.CharField(max_length=100)
    song = models.FileField(upload_to="protected-songs/",
                            max_length=250, null=True, default=None)
    songs_image = models.FileField(
        upload_to="protected-songs-photo/", max_length=250, null=True, default=None)
    sharedBy = models.CharField(max_length=50)


# Create your models here.
