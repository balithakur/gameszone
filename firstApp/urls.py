from django.contrib import admin
from django.urls import path
from firstApp import views

urlpatterns = [
    path("", views.landingpage, name='landingpage'),
    path("home", views.homepage, name="homepage" ),
    path("login", views.loginpage, name="loginpage" )
]