# Generated by Django 4.2.1 on 2023-06-10 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_service', '0006_roomservice_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='LangChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('ko', 'Korean'), ('en', 'English'), ('ja', 'Japanese'), ('cn', 'Chinese')], default='ko', max_length=2)),
                ('room_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='roomservice',
            name='category',
            field=models.CharField(choices=[('FNB', 'Food&Beverage'), ('BAS', 'Bath Amenity'), ('BED', 'Bedclothes'), ('ETC', 'Etc')], default='FNB', max_length=20),
        ),
    ]