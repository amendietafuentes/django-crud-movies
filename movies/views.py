from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def movies(request):
    return render(request, 'movies/index.html')
def add(request):
    return render(request, 'movies/create.html')
def edit(request):
    return render(request, 'movies/edit.html')