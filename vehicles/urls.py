from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('search', views.search, name="search"),
    path('sellCar', views.sellCar, name="sellCar"),
    path('filter', views.filter, name="filter"),
    path('compare', views.compare, name="compare"),    
    path('specifications', views.specifications, name="specifications"),
]
