# Generated by Django 4.2.1 on 2023-06-10 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_service', '0007_langchoice_alter_roomservice_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomservice',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
