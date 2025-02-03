from django.shortcuts import render
from django.http import HttpResponse
varia = {}
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
    dias = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Inválido']
    if dia > 7 or dia <1:
        return render(request,'semana.html',{'dia':'Dia inválido'})
    for i in range(dia):
        return render(request,'semana.html',{'dia':dias[i-1]})
def dados(request):
    global varia 
    context = varia
    return render(request,'dados.html',context)
def form(request):
    if request.method == "POST": 
        global varia
        # captura cada informação digitada no formulário
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        cidade = request.POST.get("cidade")
        RG = request.POST.get('RG')
        CPF = request.POST.get('CPF')
        telefone = request.POST.get('telefone')
        email = request.POST.get('e-mail')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        estado = request.POST.get('estado')
        CEP = request.POST.get('CEP')
        # cria um dicionário context com os dados capturados
        context = {
            'nome': nome,
            'idade': idade,
            'cidade': cidade,
            'RG':RG,
            'CPF':CPF,
            'telefone':telefone,
            'email':email,
            'rua':rua,
            'numero':numero,
            'bairro':bairro,
            'estado':estado,
            'CEP':CEP

        }
        varia = context
        # mostra os dados capturados no template dados.html
        return render(request,'dados.html',context)
    else: # method GET, mostra o formulário vazio
        return render(request,'form.html')
