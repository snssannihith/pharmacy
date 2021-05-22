from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from app1 import views

urlpatterns = [
     path('', views.index, name='index'),
     path('about', views.about, name='about'),
     path('services', views.services, name='services'),
     path('contact', views.contact, name='contact')
]