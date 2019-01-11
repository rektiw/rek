from django.contrib import admin
from django.urls import path
from apps.views import *



urlpatterns = [
    path('success/', success, name="success"),
    path('home/',home, name="home"),
    path('Gmail/',Gmail, name="Gmail"),
    path('index/',index, name="index"),
    path('main/', main, name="main"),
    path('New/', Newuser, name="Newuser")
   #path('Registration/', Registration, name="Registration"),
    

  ]

    
