from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('HOME_DS')
    return render(request, 'recipes/home.html')


def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')