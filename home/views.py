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