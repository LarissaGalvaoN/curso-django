from django.shortcuts import render

def home (request):
    #busca o template na pasta template automaticamente
    return render(request, 'recipes/home.html')


