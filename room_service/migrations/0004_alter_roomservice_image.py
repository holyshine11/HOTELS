# Generated by Django 4.2.1 on 2023-06-07 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_service', '0003_alter_roomservice_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomservice',
            name='image',
            field=models.ImageField(blank=True, upload_to='Hotels//room_service//static//room_service//'),
        ),
    ]
