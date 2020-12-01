from django.http import HttpResponse
from django.shortcuts import render

from news.models import News


def index (request):
    new=News.objects.all()
    context={
        'news':new,
        'title':'Serg Shop News'
    }
    return render(request,'news/index.html',context)
