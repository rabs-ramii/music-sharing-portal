# Generated by Django 4.1.7 on 2023-06-17 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0008_remove_song_id_alter_song_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='users_email',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
    ]
