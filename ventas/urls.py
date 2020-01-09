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
    path('registrarme', views.registrarme, name="registrarme"),
    path('ingresar', auth_views.LoginView.as_view(template_name="ventas/ingresar.html"), name="ingresar"),
    path('salir', auth_views.LogoutView.as_view(next_page='ingresar'), name='salir'),
]