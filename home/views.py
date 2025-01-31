from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def sobre(request):
    return render(request,'sobre.html')
def contato(request):
    return render(request,'contato.html')
def ajuda(request):
    return render(request,'ajuda.html')
def local(request):
    return render(request,'local.html')
def exibiritem(request,id):
    return render(request,'exibiritem.html',{'id':id})
def perfil(request,nome):
    return render(request,'perfil.html',{'nome':nome})
def semana(request,dia):
    if dia > 7 or dia <1:
        return render(request,'semana.html',{'dia':'Dia inválido'})
    if dia == 1:
        return render(request,'semana.html',{'dia':'Domingo'})
    if dia == 2:
        return render(request, 'semana.html',{'dia':'segunda feira'})
    if dia == 3:
        return render(request, 'semana.html',{'dia':'terça feira'})
    if dia == 4:
        return render(request, 'semana.html',{'dia':'quarta feira'})
    if dia == 5:
        return render(request, 'semana.html',{'dia':'quinta feira'})
    if dia == 6:
        return render(request, 'semana.html',{'dia':'sexta feira'})
    if dia == 7:
        return render(request, 'semana.html',{'dia':'sábado'})