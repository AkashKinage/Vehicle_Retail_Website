# Generated by Django 4.0.4 on 2022-05-10 07:22

from django.db import migrations, models
import vehicles.models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0008_documents_alter_usedvehicle_id_alter_vehicle_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='insurance',
            field=models.FileField(null=True, upload_to=vehicles.models.get_upload_path),
        ),
        migrations.AlterField(
            model_name='documents',
            name='invoice',
            field=models.FileField(null=True, upload_to=vehicles.models.get_upload_path),
        ),
        migrations.AlterField(
            model_name='documents',
            name='puc',
            field=models.FileField(null=True, upload_to=vehicles.models.get_upload_path),
        ),
        migrations.AlterField(
            model_name='documents',
            name='rc',
            field=models.FileField(null=True, upload_to=vehicles.models.get_upload_path),
        ),
    ]
