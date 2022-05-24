from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    cover = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Cover')
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(null=True, verbose_name='Description')

def __str__(self):
    row = "Title: " + self.title + " - " + "Description: " + self.description
    return row 

def delete(self, using=None, keep_parents=False):
    self.cover.storage.delete(self.cover.name)
    super().delete()
