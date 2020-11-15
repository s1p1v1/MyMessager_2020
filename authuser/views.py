from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse

from messager.models import Sender, Contacts

# Create your views here.
"""
def login(request):
    '''Вход пользователя в коммуникатор'''
    comment = 'Страница входа'
    content = {'comment': comment}
    return render(request, 'login.html', content)
"""

def register(request):
    '''Регистрация пользователя в коммуникаторе'''
    if request.method != 'POST':
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)

    if form.is_valid():
        new_user = form.save()
        # Добавление нового пользователя в таблицу получателей
        Sender(owner_id=new_user.id).save()

        # Создание для него списка контактов
        c = Contacts(owner=new_user)
        c.save()

        auth_user = authenticate(username=new_user.username, password=request.POST['password1'])
        login(request, auth_user)
        return HttpResponseRedirect(reverse('messager:contacts'))

    comment = 'Страница регистрации'
    content = {'comment': comment, 'form': form}
    return render(request, 'register.html', content)

def login(request):
    '''Вход пользователя в коммуникатор'''
    form = AuthenticationForm(data=request.POST)

    if request.method == 'POST' and form.is_valid():

        auth_user = authenticate(username=request.POST['username'], password=request.POST['password'])
        auth.login(request, auth_user)

        # Устанавливается признак online
        login_sender = Sender.objects.get(participant=auth_user)
        print(auth_user, login_sender)
        login_sender.online = True
        login_sender.save()
        return HttpResponseRedirect(reverse('messager:contacts'))

    comment = 'Страница входа'
    content = {'comment': comment, 'form': form}
    return render(request, 'login.html', content)

def logout(request):
    '''Выход пользователя из коммуникатора'''
    logout_sender = Sender.objects.get(participant=request.user)
    logout_sender.online = False
    logout_sender.save()
    print(request.user, logout_sender.online)
    auth.logout(request)
    return HttpResponseRedirect(reverse('messager:home'))