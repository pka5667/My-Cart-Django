# Generated by Django 3.2 on 2021-04-26 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
