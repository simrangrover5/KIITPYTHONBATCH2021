from django.http import HttpResponse 

def index(request):
    return HttpResponse("Hello world")

def home(request):
    return HttpResponse("<h1 style='color:red'>This is My Home of Python</h1>")