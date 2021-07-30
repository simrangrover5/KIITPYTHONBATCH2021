from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index),
    path("register/", views.register),
    path("aftersignup/", views.aftersignup),
    path("signin/", views.signin),
]