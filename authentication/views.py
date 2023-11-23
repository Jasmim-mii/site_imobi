from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'register.html')
    elif request.method == 'POST':
        username_register = request.POST.get('username_register')
        email_register = request.POST.get('email_register')
        password_register = request.POST.get('password_register')

        if len(username_register.strip()) == 0 or len(email_register.strip()) == 0 or len(password_register.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/auth/register')
        user = User.objects.filter(username=username_register)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome cadastrado')
            return redirect('/auth/register')

        try:
            user = User.objects.create_user(username=username_register, email=email_register, password=password_register)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso')
            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/auth/register')

        # return HttpResponse(f'{username_register} {email_register} {password_register}')
    # return render(request, 'cadastro.html')


def login(request):

    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')
    elif request.method == "POST":
        username_login = request.POST.get('username_login')
        password_login = request.POST.get('password_login')

    username_login = auth.authenticate(username=username_login, password=password_login)

    if not username_login:
        messages.add_message(request, constants.ERROR, 'Username ou Senha invalido')
        return redirect('/auth/login')
    else:
        auth.login(request, username_login)
        return redirect('/')


def sair(request):
    auth.logout(request)
    return redirect('/auth/login')


