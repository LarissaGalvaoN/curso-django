from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    #busca o template na pasta template automaticamente
    return render(request, 'recipes/home.html')

def contato (request):
    return HttpResponse('Contato9')

def sobre (request):
    return HttpResponse('Sobre9')
