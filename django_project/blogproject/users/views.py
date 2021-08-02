from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import Register, Login, GetEmail
from .models import AddUser
from django.views import View
from random import randint
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    if request.session.get("islogin"):
        return render(request, "afterlogin.html")
    return render(request, "nav.html")

def register(request):
    if request.session.get("islogin"):
        return render(request, "afterlogin.html")
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
            try:
                AddUser.objects.get(email=email)
            except: # we will get if the user does not exists then we will add its details
                AddUser.objects.create(fname=fname, lname=lname, email=email, password=password)
                msg = "Registered Successfully...."
                form = Login()
                return render(request, "login.html", {'msg': msg, 'form': form})
            else: # here we will have no error that means user already exists....
                msg = "User Already Exists.."
                form = Register()
                return render(request, "register.html", {'msg': msg, 'form': form})
            # return HttpResponse(f"{email} --> {password}")
        else:
            msg = "Please Fill The Entries Correctly"
            form = Register()
            return render(request, "register.html", {'form': form, 'msg': msg})
        
def signin(request):
    f = Login()
    return render(request, "login.html", {'form': f})

class Afterlogin(View):
    def get(self, request):
        return redirect("/signin/")
    
    def post(self, request):
        form = Login(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                obj = AddUser.objects.get(email=email)
            except: # if error comes that means user does not exists
                msg = "User Does Not Exists..."
                form = Register()
                return render(request, "register.html", {'form': form, 'msg': msg})
            else:
                if obj.password == password:
                    request.session['islogin'] = "true"
                    return render(request, "afterlogin.html")
                else:
                    msg = "Please Fill Password Correct..."
                    form = Login()
                    return render(request, "login.html", {'form': form, 'msg': msg})

        else:
            msg = "Please Fill Entries Correct..."
            form = Login()
            return render(request, "login.html", {'form': form, 'msg': msg})

def logout(request):
    del request.session['islogin']
    return redirect("/")

def forgot(request):
    form = GetEmail()
    return render(request, "getemail.html", {"form": form})

class CheckEmail(View):
    def get(self, request):
        return redirect("/signin/")

    def post(self, request):
        form = GetEmail(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                AddUser.objects.get(email=email)
            except:
                msg = "No such email exist..."
                form = Login()
                return render(request, "login.html", {"form": form, "msg": msg})
            else:
                otp = randint(1000, 9999)
                from_email = "simrangrover1601@gmail.com"
                to_email = email 
                subject = "BLOGWEBSITE: OTP for forgot password"
                msg = f"OTP to change your password is {otp}"
                try:
                    send_mail(subject, msg, from_email, [to_email], auth_password=settings.EMAIL_HOST_PASSWORD)
                except Exception as error:
                    return HttpResponse(f"{error}")
                else:
                    request.session['otp'] = otp 
                    request.session['email'] = email
                    return render(request, "getotp.html")

class Getotp(View):
    def get(self, request):
        del request.session['otp']
        del request.session['email']
        return redirect("/signin/")
    
    def post(self, request):
        otp_ = request.POST.get("otp")
        if otp_ == request.session['otp']:
            return render(request, "newpass.html")
        else:
            del request.session['otp']
            del request.session['email']
            return redirect("/signin/")

#  obj = AddUser.objects.get(email=request.session.get('email'))
# obj.password = newpass
# obj.save()
