from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    cover = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Cover')
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(null=True, blank=True, max_length=500, verbose_name='Description')


