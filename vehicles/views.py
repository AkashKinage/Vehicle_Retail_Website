from django.http import HttpResponse
from django.shortcuts import render
from .models import Vehicle, UsedVehicle, Documents
import datetime
from decimal import Decimal as D
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def search(request):
    query = request.GET['query']
    # vehicles = Vehicle.objects.filter(vehicle_name__icontains=query)
    vehicles = UsedVehicle.objects.filter(model_name__icontains=query)
    params = {'vehicles':vehicles}
    
    
    return render(request, 'search.html', params)

# def filter(request):
#     brand = request.GET['brand']
#     price = D(request.GET['price'])
#     print(type(price))
    
#     # vehicles = UsedVehicle.objects.filter(brand__icontains=brand)
#     vehicles = UsedVehicle.objects.filter(price__range=(0, price))
#     params = {'vehicles':vehicles}
#     return render(request, 'search.html', params)
        
def filter(request):
    if request.GET['brand']:
        brand = request.GET['brand']
        price = D(request.GET['price'])
        
        if brand !='default' and price == 0:
            vehicles = UsedVehicle.objects.filter(brand__icontains=brand)
            params = {'vehicles':vehicles}
            return render(request, 'search.html', params)
        
        elif brand == 'default' and price != 0:
            vehicles = UsedVehicle.objects.filter(price__range=(0, price))
            params = {'vehicles':vehicles}
            return render(request, 'search.html', params)
        
        elif brand != 'default' and price != 0:
            vehicles = UsedVehicle.objects.filter(brand__icontains=brand,price__range=(0, price))
            params = {'vehicles':vehicles}
            return render(request, 'search.html', params)
        else:
            vehicles = UsedVehicle.objects.filter(brand__icontains=brand)
            params = {'vehicles':vehicles}
            return render(request, 'search.html', params)

def compare(request):
    if request.GET.get('car1','') and request.GET.get('car2',''):
        car1 = request.GET.get('car1','')
        car2 = request.GET.get('car2','')
        if car1 != car2:
            vehicle1 = UsedVehicle.objects.filter(model_name__icontains=car1)
            vehicle2 = UsedVehicle.objects.filter(model_name__icontains=car2)
            params = {'vehicle1':vehicle1,'vehicle2':vehicle2}
            if vehicle1 and vehicle2:
                # print("Yes")
                return render(request,'compare.html',params)
            else:
                # print("No")
                messages.error(request,'Vehicles not available')    
            # print(vehicle2)
            return render(request,'compare.html',params)
        else:
            messages.error(request,'Can not compare same vehicles')
            return redirect('compare')
    else:
        return render(request,'compare.html')

def sellCar(request):
    if request.method == 'POST' and request.FILES['carImages']:
    #if request.method == "POST":
        user = request.user.username
        brand = request.POST['brand']
        model = request.POST['model']
        carType = request.POST['type']
        price = request.POST['price']
        registrationYear = request.POST['registrationYear']
        fuelType = request.POST['fuelType']
        transmission = request.POST['transmission']
        engineCapacity = request.POST['engineCapacity']
        ownership = request.POST['ownership']
        kilometersDriven = request.POST['kilometersDriven']
        description = request.POST['description'] 
        carImages = request.FILES['carImages']

        rc = request.FILES['rc']
        puc = request.FILES['puc']
        insurance = request.FILES['insurance']
        invoice = request.FILES['invoice']

        documents = Documents(user=request.user,model_name=model,rc=rc,puc=puc,insurance=insurance,invoice=invoice)
        documents.save()
        
        # print(user,brand,model,carType,ownership)
        
        usedVehicle = UsedVehicle(model_name=model,seller=user,brand=brand,carType=carType,price=price,registrationYear=registrationYear,fuelType=fuelType,transmission=transmission,engineCapacity=engineCapacity,ownership=ownership,kilometersDriven=kilometersDriven,description=description,datePosted=datetime.date.today(),carImages=carImages)
        usedVehicle.save()
    return render(request,'sellcar.html')

def specifications(request):
    query = request.GET['parameter']
    vehicles = UsedVehicle.objects.filter(model_name__icontains=query)
    documents = Documents.objects.filter(model_name__icontains=query)
    params = {'vehicles':vehicles,'documents':documents}
    return render(request, 'specifications.html', params)
    