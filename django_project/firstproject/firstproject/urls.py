"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from . import views # . --> PWD 

urlpatterns = [
    path('admin/', admin.site.urls),  # admin panel
    path("", views.index),  # / --> domain , "" --> domain
    path("home/", views.home), # localhost/home/ --> views --> home
    path("app1/", include("app1.urls")) # whenever we get request for localhost/app1/
                                        # we can redirect it to app1.urls
]
