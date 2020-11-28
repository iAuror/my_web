from django.http import HttpResponse
from django.shortcuts import render

def buy(request):
    return HttpResponse('Buy Doors')
