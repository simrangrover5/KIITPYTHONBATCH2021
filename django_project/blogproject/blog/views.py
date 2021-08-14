from django.shortcuts import render, redirect
from .forms import Blog
from django.views import View
from .models import Addblog
from users.models import AddUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ShowBlog
# Create your views here.
def addblog(request):
    form = Blog()
    return render(request, "addblog.html", {'form': form})

class Submitblog(View):
    def get(self, request):
        return redirect("/blog/addblog/")

    def post(self, request):
        form = Blog(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            post = form.cleaned_data['post']
            category = form.cleaned_data['categories']
            author = AddUser.objects.get(email=request.session.get("email"))
            Addblog.objects.create(title=title, post=post, cat=category, author=author)
            msg = "Blog Successfully Added"
            return render(request, "afterlogin.html", {'msg': 'msg'})
        else:
            msg = "Please fill the entries correct"
            form = Blog()
            return render(request, "addblog.html", {'form':form, 'msg':msg})

def allblogs(request):
    all_ = Addblog.objects.all()
    return render(request, "blogs.html", {'all': all_})

def myblog(request):
    my = Addblog.objects.filter(author=AddUser.objects.get(email=request.session.get("email")))
    return render(request, "blogs.html", {'all': my})

class MyAPI(APIView):
    def get(self, request): # get method request of API
        all_ = Addblog.objects.all()
        blogs = ShowBlog(all_, many=True)
        return Response(blogs.data)

    def post(self, request):
        pass 


