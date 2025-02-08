"""
URL configuration for pweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('sobre',views.sobre,name='sobre'),
    path('contato',views.contato,name='contato'),
    path('ajuda',views.ajuda,name='ajuda'),
    path('local',views.local,name='local'),
    path('exibiritem/<int:id>',views.exibiritem,name='exibiritem'),
    path('perfil/<str:nome>',views.perfil,name='perfil'),
    path('diadasemana/<int:dia>',views.semana,name='semana'),
    path('dados/',views.dados,name='dados'),
    path('form/',views.form,name='form'),
    path('alunos/listar/',views.listar_aluno,name='listar_aluno'),
    path('alunos/editar/<int:indice>',views.editar_aluno,name='editar_aluno'),

    path('alunos/excluir/<int:indice>',views.remover_aluno,name='remover_aluno'),
    path('alunos/cadastrar/',views.cadastrar_aluno,name='cadastrar_aluno'),

    path('alunos/excluir/<int:indice>',views.remover_aluno,name='remover_aluno')

]
