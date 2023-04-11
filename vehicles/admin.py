from django.contrib import admin
from .models import Vehicle, UsedVehicle, Documents
# Register your models here.
admin.site.register(Vehicle)
admin.site.register(UsedVehicle)
admin.site.register(Documents)