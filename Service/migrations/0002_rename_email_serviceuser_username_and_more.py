# Generated by Django 4.1.7 on 2023-06-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceuser',
            old_name='email',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='serviceuser',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
