from django.urls import path, include
from . import views

urlpatterns = [
    path("addblog/", views.addblog),  # localhost/blog/addblog
    path("submitblog/", views.Submitblog.as_view()),
    path("allblogs/", views.allblogs),
    path("myblog/", views.myblog),
    path("api/", views.MyAPI.as_view())
]