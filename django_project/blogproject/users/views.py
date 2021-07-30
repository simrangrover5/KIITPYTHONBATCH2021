from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import Register, Login
# Create your views here.
def index(request):
    return render(request, "nav.html")

def register(request):
    f = Register()
    return render(request, "register.html", {'form': f})

def aftersignup(request):
    if request.method == "GET":
        return redirect("/register/")
    else:
        form = Register(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            return HttpResponse(f"{email} --> {password}")
        else:
            msg = "Please Fill The Entries Correctly"
            form = Register()
            return render(request, "register.html", {'form': form, 'msg': msg})
        
def signin(request):
    f = Login()
    return render(request, "login.html", {'form': f})