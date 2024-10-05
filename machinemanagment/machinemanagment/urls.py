"""
URL configuration for machinemanagment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from machinemanagment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('maquinaria/', views.maquinaria, name='maquinaria'),  # Ruta para la página de maquinaria
    path('inventario/', views.inventario, name='inventario'),  # Ruta para la página de inventario
    path('status/', views.status, name='status'),  # Ruta para la página de inventario
    path('empresa/', views.empresa, name='empresa'),  # Ruta para la página de inventario
    path('empleados/', views.empleados, name='empleados'),  # Ruta para la página de inventario
    path('home/', views.home, name='home'),  # Ruta para la página de inventario

]
