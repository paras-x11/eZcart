# Generated by Django 5.1.4 on 2025-03-20 02:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_price_orderitem_orderprice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.address'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='orderPrice',
            field=models.FloatField(),
        ),
    ]
