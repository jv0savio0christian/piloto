from django.shortcuts import redirect, render
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
LISTA_ALUNOS = [
    {"nome": "João Silva",'data_nascimento': '03/10/2009', "matricula": "202301", "curso": "Técnico em Informática", "turma": "208"},
    {"nome": "Maria Oliveira", 'data_nascimento': '05/02/2008', "matricula": "202302", "curso": "Técnico em Informática", "turma": "208"},
    {"nome": "Carlos Souza", 'data_nascimento': '20/12/2009', "matricula": "202303", "curso": "Técnico em Informática", "turma": "208"},
]
def listar_aluno(request):
    context = {
        'lista': LISTA_ALUNOS,
    }
    return render(request,'listar_aluno.html',context)
def editar_aluno(request,indice):
    aluno=LISTA_ALUNOS[indice]
    if request.method == "POST":
        aluno['nome'] = request.POST.get('nome')
        aluno['matrícula'] = request.POST.get('matrícula')
        aluno['data_nascimento'] = request.POST.get('data_nascimento')
        aluno['curso'] = request.POST.get('curso')
        aluno['turma'] = request.POST.get('turma')
        return redirect('listar_aluno')
    context={
        'aluno':aluno,
        'indice':indice
}
    return render(request,'form_aluno.html',context)



def remover_aluno(request,indice):
    del LISTA_ALUNOS[indice]
    return redirect('listar_aluno')

def cadastrar_aluno(request):
    if request.method=="POST":
        nome=request.POST.get('nome')
        matricula=request.POST.get('matricula')
        curso=request.POST.get('curso')
        turma=request.POST.get('turma')
        data_nascimento=request.POST.get('data_nascimento')

        novo_aluno= {
            "nome":nome,
            "matricula":matricula,
            "curso":curso,
            "turma":turma,
            "data_nascimento":data_nascimento
        }
        LISTA_ALUNOS.append(novo_aluno)
        return redirect('listar_aluno')
    
    return render(request,'form_aluno.html')


def remover_aluno(request,indice):
    del LISTA_ALUNOS[indice]
    return redirect('listar_aluno')

