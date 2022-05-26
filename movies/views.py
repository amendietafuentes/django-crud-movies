from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm

# Create your views here.

#Get all movies
def movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies' : movies})

def add(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if (form.is_valid()):
        form.save()
        return redirect('movies')
    return render(request, 'movies/create.html', {'form' : form})

def edit(request, id):
    movies = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movies)
    if (form.is_valid() and request.POST):
        form.save()
        return redirect('movies')
    return render(request, 'movies/edit.html', {'form' : form})

def delete(request, id):
    movies = Movie.objects.get(id=id)
    movies.delete()
    return redirect('movies')

