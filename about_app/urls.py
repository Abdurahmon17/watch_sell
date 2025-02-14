from django.urls import path
from .views import main

urlpatterns = [
    path('about/', main, name='About'),
]