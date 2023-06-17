from django.shortcuts import render
from django.http import HttpResponse
from .views import index
from django.urls import path, include

urlpatterns = [
    path('', index,name='home/index')
]
