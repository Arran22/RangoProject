from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! <a href='http://localhost:8000/about'>about</a>")

def about(request):
    return HttpResponse("<a href='http://localhost:8000'>index</a>")

