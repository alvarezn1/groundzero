from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request):
    context={}
    return render(request, 'groundzero/index.html', context)

def Artistas(request):
    context={}
    return render (request,'groundzero/Artistas.html',context)

def catalogo(request):
    context={}
    return render (request,'groundzero/catalogo.html',context)

def contacto(request):
    context={}
    return render (request,'groundzero/contacto.html',context)

def login(request):
    context={}
    return render (request,'groundzero/login.html',context)

def registro(request):
    context={}
    return render (request,'groundzero/registro.html',context)
