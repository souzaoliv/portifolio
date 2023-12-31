from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Formulario, Projetos, ProjetosTags, ProjetosFuncionalidades, Tags, Funcionalidades
from . formulario import FormularioCadastro
# Create your views here.
def index(request):
    projetos = Projetos.objects.all()
    if projetos.exists():
        for projeto in projetos:
            projeto.tags = projeto.projetostags_set.all()
            projeto.funcionalidades = projeto.projetosfuncionalidades_set.all()
        context = {'projetos': projetos}

    else:
        context = {}
    if request.method == "GET":
        return render(request, 'portifolio/index.html', context)
    if request.method == "POST":
        formulario = FormularioCadastro(request.POST)
        if formulario.is_valid():
            formulario.save()
            sucesso = "Seus dados foram enviados com sucesso."
            return render(request, 'portifolio/index.html', {'sucesso': sucesso})
        else:
            erro = "Não foi possivel enviar o formulario, Retorne e reenvie por favor."
        return render(request, 'portifolio/index.html', {'erro': erro})
    else:
        return render(request, 'portifolio/index.html', context)







