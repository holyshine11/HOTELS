# Generated by Django 4.2.3 on 2023-07-26 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_service', '0011_cart_product_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='quantity',
        ),
    ]