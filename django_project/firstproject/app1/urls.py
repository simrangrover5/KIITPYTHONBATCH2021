from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.index) # "" --> localhost/app1/
]