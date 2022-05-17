from django.urls import path
from . import views

urlpatterns = [
    path('movies', views.movies, name='movies'),
    path('movies/add', views.add, name='add'),
    path('movies/edit', views.edit, name='edit'),
]