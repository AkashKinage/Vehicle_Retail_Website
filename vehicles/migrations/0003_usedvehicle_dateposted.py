# Generated by Django 3.1.1 on 2022-03-19 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_usedvehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='usedvehicle',
            name='datePosted',
            field=models.DateField(default=datetime.date.today),
        ),
    ]