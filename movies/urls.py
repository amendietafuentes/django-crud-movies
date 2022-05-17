from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about-us', views.about, name='about'),
    path('movies', views.movies, name='movies'),
]