"""
URL configuration for aton_test project.

The `urlpatterns` list routes URLs to views. For more information please see:

"""
from django.contrib import admin
from django.urls import path, include
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('clients.urls')),
]


