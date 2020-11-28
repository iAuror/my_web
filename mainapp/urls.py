from django.urls import path

from mainapp.views import buy

urlpatterns = [
    path ('buy/', buy)
]