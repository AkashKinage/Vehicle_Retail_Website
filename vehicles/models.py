from distutils.command.upload import upload
from django.db import models
import datetime
from django.utils import timezone
today = timezone.now

# Create your models here.
class Vehicle(models.Model):
    vehicle_id = models.AutoField
    vehicle_name = models.CharField(max_length=255)
    vehicle_description = models.TextField()
    vehicle_type = models.CharField(max_length=255)
    vehicle_price = models.IntegerField()
    vehicle_image = models.ImageField(upload_to="vehicles/images")
    
class UsedVehicle(models.Model):
    model_name = models.CharField(max_length=255)
    id = models.AutoField
    seller = models.CharField(max_length=255) 
    brand = models.CharField(max_length=255)
    carType = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    registrationYear = models.CharField(max_length=255)
    fuelType = models.CharField(max_length=255)
    transmission = models.CharField(max_length=255)
    engineCapacity = models.CharField(max_length=255)
    ownership = models.CharField(max_length=255)
    kilometersDriven = models.CharField(max_length=255)
    description = models.TextField()
    datePosted = models.DateField(default=today)
    carImages = models.ImageField(upload_to="vehicles/images")

    def __str__(self):
        return self.model_name

def get_upload_path(instance, filename):
    return 'documents/{0}/{1}'.format(instance.user.username, filename)

class Documents(models.Model):
    user = models.CharField(max_length=255) 
    model_name = models.CharField(max_length=255,default='default')
    rc = models.FileField(null=True,upload_to=get_upload_path)
    puc = models.FileField(null=True,upload_to=get_upload_path)
    insurance = models.FileField(null=True,upload_to=get_upload_path)
    invoice = models.FileField(null=True,upload_to=get_upload_path)

    def __str__(self):
        return self.model_name

    # rc = models.FileField(null=True,upload_to="documents/")
    # puc = models.FileField(null=True,upload_to="documents/")
    # insurance = models.FileField(null=True,upload_to="documents/")
    # invoice = models.FileField(null=True,upload_to="documents/")
