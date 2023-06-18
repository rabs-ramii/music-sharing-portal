# Generated by Django 4.1.7 on 2023-06-17 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0004_alter_songs_song_alter_songs_songs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='song',
            field=models.FileField(max_length=250, upload_to='songs/'),
        ),
        migrations.AlterField(
            model_name='songs',
            name='songs_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='song-photo/'),
        ),
        migrations.AlterField(
            model_name='songs',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]