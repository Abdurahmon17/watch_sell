from django.urls import path
from .views import contact_view
from django.shortcuts import render

urlpatterns = [
    path('contact/', contact_view, name='Contact'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),
]
