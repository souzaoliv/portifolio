from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login , logout
from django.views.decorators.http import require_http_methods

from .models import Tarefa

# Create your views here.
def index(request):
    return render(request, 'lista_de_tarefas/index.html')


def cadastrar(request):
    ...

def logar(request):
    ...

def deslogar(request):
    ...

def exibir_tarefas(request):
    ...

def criar_tarefa(request):
    ...
def editar_tarefa(request, pk):
    ...
def excluir_tarefa(request, pk):
    ...



