# Generated by Django 3.1.1 on 2022-03-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsedVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=255)),
                ('seller', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('carType', models.CharField(max_length=255)),
                ('registrationYear', models.CharField(max_length=255)),
                ('fuelType', models.CharField(max_length=255)),
                ('transmission', models.CharField(max_length=255)),
                ('engineCapacity', models.CharField(max_length=255)),
                ('ownership', models.CharField(max_length=255)),
                ('kilometersDriven', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('carImages', models.ImageField(upload_to='vehicles/images')),
            ],
        ),
    ]
