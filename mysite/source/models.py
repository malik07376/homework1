import django
from django.db import models
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
# Create your models here.

class Director(models.Model):
    director_name=models.CharField(max_length=30)
    age=models.IntegerField()
    bio=models.TextField()
    def __str__(self):
        return self.director_name
class Actor(models.Model):
    actor_name=models.CharField(max_length=30)
    age=models.IntegerField()
    bio=models.TextField()
    # actor_image=models.ImageField(upload_to='#')

    def __str__(self):
        return self.actor_name