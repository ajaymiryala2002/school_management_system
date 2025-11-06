from django.shortcuts import render
from django.http import HttpResponse

def wish(request):
    return HttpResponse('Welcome to django project')
