from django.shortcuts import render
from django.http import HttpResponse

def hyd(request):
    x="Hyderabad provides free courses"
    return HttpResponse(x)

def bang(request):
    y="Banglore provides job for everyone"
    return HttpResponse(y)

def chen(request):
    z="Chennai provides job to only local people"
    return HttpResponse(z)
