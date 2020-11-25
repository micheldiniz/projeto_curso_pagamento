from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from cursos_pagamento.forms import SetorForms, ServidorForms, CursoForms
from cursos_pagamento.models import Atividade, Curso, Setor, Usuario, User


def index(request):
    return render(request, 'index.html')

def login_pagina(request):
    return render(request, 'login.html')

def logout_pagina(request):
    auth.logout(request)
    return redirect('index')

def login(request):
    """Realiza o login"""
    if request.method == 'POST':
        username = request.POST['user']
        print(username)
        password = request.POST['senha']
        print(password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('Login OK')
            return redirect('dashboard') 
    return render(request, 'login.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('index')

def pagina_setor(request):    
    """    docstring    """
    if request.user.is_authenticated:
        setor_form = SetorForms()
        contexto = {'setor_form': setor_form}
        return render(request, 'cadastros/setor.html', contexto)
    else:
        return redirect('index')

def pagina_servidor(request):
    """    docstring    """
    if request.user.is_authenticated:
        servidor_form = ServidorForms()
        contexto = {'servidor_form': servidor_form}
        return render(request, 'cadastros/servidor.html', contexto)
    else:
        return redirect('index')

def pagina_curso(request):
    """    docstring    """
    if request.user.is_authenticated:
        curso_form = CursoForms()
        contexto = {'curso_form': curso_form}
        return render(request, 'cadastros/curso.html', contexto)
    else:
        return redirect('index')

def cadastro_setor(request):
    if request.method == 'POST':
        form = SetorForms(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            sigla = form.cleaned_data['sigla']
            setor = Setor.objects.create(nome=nome, sigla=sigla)
            setor.save()
            setores = Setor.objects.all()
            contexto = {'setores':setores}
        return render(request, 'setores/visualiza.html', contexto)
    else:
        return render(request, 'cadastros/setor.html')

def deleta_setor(request, setor_id):
    obj = get_object_or_404(Setor, pk=setor_id)
    obj.delete()
    setores = Setor.objects.all()
    contexto = {'setores': setores}
    return render(request, 'setores/visualiza.html', contexto)

def cadastro_servidor(request):
    if request.method == 'POST':
        form = ServidorForms(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            matricula = form.cleaned_data['matricula']
            setor = get_object_or_404(Setor, pk=request.POST['setor'])
            login = form.cleaned_data['login']
            is_chefe = form.cleaned_data['is_chefe']
            servidor = Usuario.objects.create(
            nome=nome,
            matricula=matricula,
            setor=setor,
            login=login,
            is_chefe=is_chefe)
            servidor.save()
            return redirect('dashboard')        
        else:
            form = ServidorForms()
    else:
        return render(request, 'cadastros/servidor.html')

def cadastro_curso(request):
    if request.method == 'POST':
        form = CursoForms(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            responsavel = get_object_or_404(Usuario, pk=request.POST['responsavel'])
            carga_horaria = form.cleaned_data['carga_horaria']
            data_inicio = form.cleaned_data['data_inicio']
            data_termino = form.cleaned_data['data_termino']
            curso = Curso.objects.create(
            nome=nome,
            responsavel=responsavel,
            carga_horaria=carga_horaria,
            data_inicio=data_inicio,
            data_termino=data_termino)
            curso.save()
            return redirect('dashboard')
        else:
            form = CursoForms()
    else:
        return render(request, 'cadastros/cursos.html')

def visualiza_setores(request):
    setores = Setor.objects.all()
    contexto = {
        'setores': setores
        }
    return render(request, 'setores/visualiza.html', context=contexto)


def edita_setores(request, setor_id):
    setor = get_object_or_404(Setor, pk=setor_id)
    form = SetorForms(request.POST or None, instance=setor)
    if form.is_valid():
        form.save()
        contexto = {'setores':Setor.objects.all()}
        return render(request, 'setores/visualiza.html', contexto)
    else:
        contexto = {'form':form, 'setor_id':setor_id}
        return render(request, 'setores/atualiza.html', contexto)
