from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return HttpResponse('Home9')

def contato (request):
    return HttpResponse('Contato9')

def sobre (request):
    return HttpResponse('Sobre9')
