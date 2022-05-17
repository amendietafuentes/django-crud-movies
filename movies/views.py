from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Bienvenidos a CRUD con Django</h1>")
def about(request):
    return render(request, 'pages/about.html')
def movies(request):
    return render(request, 'movies/index.html')