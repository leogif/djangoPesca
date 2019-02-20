from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse('<h1>Area da Home</h1>')

def produtos(resquest):
	return HttpResponse('<h1>Area de Produtos')

def clientes(request):
	return HttpResponse('<h1>Área de Clientes</h1>')