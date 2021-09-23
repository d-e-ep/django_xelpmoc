from movies.models import MovieShots
from django.test import TestCase
from django.contrib import admin
from django.urls import path,include
from django.db import models
# Create your tests here.

urlpatterns = [
    path('',MovieShots,name='models')

]


