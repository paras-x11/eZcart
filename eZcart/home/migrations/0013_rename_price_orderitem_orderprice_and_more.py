# Generated by Django 5.1.4 on 2025-03-20 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_orderitem_price_address_alter_order_shipping_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='price',
            new_name='orderPrice',
        ),
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.TextField(),
        ),
    ]
