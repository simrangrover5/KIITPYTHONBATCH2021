from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h2 style='color:red'>This is App1 of My Project</h1>")
    return render(request, "one.html")
