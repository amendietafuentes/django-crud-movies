from os import stat
from xml.dom.minidom import Document
from django.urls import path
from . import views

#Import file settings
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('movies', views.movies, name='movies'),
    path('movies/add', views.add, name='add'),
    path('movies/edit', views.edit, name='edit'),
    path('movies/delete/<int:id>', views.delete, name='delete'),
    path('movies/edit/<int:id>', views.edit, name='edit'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)