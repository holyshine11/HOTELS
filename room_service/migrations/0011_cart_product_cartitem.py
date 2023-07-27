# Generated by Django 4.2.3 on 2023-07-26 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('room_service', '0010_remove_roomservice_request_roomservice_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessions.session')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRD_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('content', models.CharField(default=True, max_length=30)),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, upload_to='midia/image/')),
                ('category', models.CharField(choices=[('FNB', 'Food&Beverage'), ('BAS', 'Bath Amenity'), ('BED', 'Bedclothes'), ('ETC', 'Etc')], default='FNB', max_length=20)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='room_service.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room_service.product')),
            ],
        ),
    ]