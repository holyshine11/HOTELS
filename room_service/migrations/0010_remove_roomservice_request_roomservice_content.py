# Generated by Django 4.2.1 on 2023-06-14 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_service', '0009_roomservice_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomservice',
            name='Request',
        ),
        migrations.AddField(
            model_name='roomservice',
            name='content',
            field=models.CharField(default=True, max_length=30),
        ),
    ]
