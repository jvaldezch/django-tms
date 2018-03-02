from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url('', views.index, name='index'),
    
]

