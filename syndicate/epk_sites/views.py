from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def syndicate(request):
    return HttpResponse('<h1>Syndicate EPK</h1>')

def antmang(request):
    return HttpResponse('<h1>Antmang EPK</h1>')

def griefcase(request):
    return HttpResponse('<h1>Antmang EPK</h1>')
