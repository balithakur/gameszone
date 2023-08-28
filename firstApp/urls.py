from django.contrib import admin
from django.urls import path
from firstApp import views

urlpatterns = [
    path("", views.landingpage, name='landingpage'),
]