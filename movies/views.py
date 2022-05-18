from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.


def movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def add(request):
    return render(request, 'movies/create.html')

def edit(request):
    return render(request, 'movies/edit.html')