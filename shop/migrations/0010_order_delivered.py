# Generated by Django 3.2 on 2021-05-01 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_order_paymentstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivered',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]