# Generated by Django 5.1.4 on 2025-03-05 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_cart_test_field_alter_cartitem_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='test_field',
        ),
    ]
