from django.shortcuts import render
from django.http import HttpResponse

def python(request):
    x="Python is very easy and simple Language"
    return HttpResponse(x)

def django(request):
    y="Django is the framework of Python"
    return HttpResponse(y)

def ui(request):
    z="ui is importsnt to develop web"
    return HttpResponse(z)
