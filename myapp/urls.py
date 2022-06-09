from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns=[
    path("", views.index ,name="index"),

    path("about", views.about ,name="about"),


    path("counter", views.counter ,name="counter"),

    path('home', views.home, name="home"),
    
    path('porto', views.porto, name="portofolio"),



]