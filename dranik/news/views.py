from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # print(request)
    return HttpResponse('<h1>Вызвали index</hq>')


def test(request):
    return HttpResponse('Вызвали тестовую страницу')