from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tienda', views.tienda, name="tienda"),
    path('producto/<int:pk>/', views.producto, name="producto"),
    path('añadir/<int:pk>/', views.añadir, name="añadir"),
    path('carro', views.carro, name="carro"),
]