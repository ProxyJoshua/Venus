from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tienda', views.tienda, name="tienda"),
    path('carro', views.carro, name="carro"),
]