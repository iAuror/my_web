from django.http import HttpResponse
from django.shortcuts import render


def buy(request):
    return HttpResponse('Buy Doors')


def detail(request, question_id):
    return HttpResponse(f'You\'re looking at question {question_id}')


def results(request, question_id):
    return HttpResponse(f'You\'re looking at the results of question {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You\'re voting on question {question_id}')
