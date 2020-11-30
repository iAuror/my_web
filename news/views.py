from django.http import HttpResponse
from django.shortcuts import render

def index (request):

    return HttpResponse ('<h1>Newspaper</h1><br>'
                         '<h2> тут будут новости </h2>')
