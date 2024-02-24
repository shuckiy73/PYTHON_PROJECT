from django.shortcuts import render
from django.http import HttpResponse


def url1(request):
    return HttpResponse("Ответ 1")


def url2(request):
    return HttpResponse("Ответ 2")
