# Generated by Django 3.2 on 2021-05-01 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_order_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paymentStatus',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
