# example/urls.py
from django.urls import path

from example.views import index
from example.views import Template


urlpatterns = [
    path('', index),
    path('template', Template)
]