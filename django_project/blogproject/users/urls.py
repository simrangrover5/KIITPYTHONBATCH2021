from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index),
    path("register/", views.register),
    path("aftersignup/", views.aftersignup),
    path("signin/", views.signin),
    path("afterlogin/", views.Afterlogin.as_view()), # as_view to let the server know that we need to find a class not a function as a view
    path("logout/", views.logout),
    path("forgot/", views.forgot),
    path("getemail/", views.CheckEmail.as_view()),
    path("getotp/", views.Getotp.as_view())
]