from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.template.loader import render_to_string

import json

from .models import Sender, Contacts, Messages
from .forms import Contact_add_Form, Talk
from .start_script import Messages, Message

# Create your views here.

# Создаем словарь сообщений
list_m = Messages()

def home(request):
    '''Начало'''
    comment = 'Вход/Регистрация'
    content = {'comment': comment}
    return render(request, 'index.html', content)
    #return HttpResponse(comment)

@login_required()
def contacts(request):
    '''Список контактов авторизованного пользователя'''
    user_name = request.user.username  # владелец контакта
    comment = 'Контакты пользователя: {}'.format(user_name)
    print('view.contacts: {} (sender)'.format(user_name))

    contacts = Contacts.objects.filter(owner=request.user)[0].sender.all()

    for i in contacts:
        if i.online:
            print(i.participant.username, '+')
        else:
            print(i.participant.username)

    # Пользователю пришли новые сообщения
    list_username_sender_messages = list_m.reception(request.user)
    print('новые сообщения', list_username_sender_messages)

    if request.is_ajax():
        print('contacts ajax request')
        content1 = {'contacts': contacts, 'messages': list_username_sender_messages}
        result = render_to_string('messager/templates/contacts/inc_contacts_list.html', content1)
        return JsonResponse({'result': result})
    else:
        print('not ajax request')
        content = {'comment': comment, 'contacts': contacts}
        return render(request, 'messager/templates/contacts/contacts.html', content)

@login_required()
def add_contact(request):
    '''Добавление контакта авторизованным пользователем'''
    #contact_owner = get_user(request)
    contact_owner = request.user  # владелец контакта
    contact_owner_name = contact_owner.username
    print('view.add_contact: {} (sender)'.format(contact_owner_name))

    # создать пустую форму
    if request.method != 'POST':
        contacts_form = Contact_add_Form()

    # отправить данные на сервер
    else:
        contacts_form = Contact_add_Form(data=request.POST)
        if contacts_form.is_valid():
            #contacts_form.save()
            user_name = contacts_form.cleaned_data.get('contact_name')
            #user_name = contacts_form.fields['contact_name'].label
            print(contacts_form.cleaned_data)
            print('Добавляемый контакт', user_name)
            # contact_owner = Sender.objects.get(owner=user)
            user = User.objects.get(username=user_name)
            new_contact = Sender.objects.get(participant=user)
            print('Владелец контакта', contact_owner_name)

            cc = Contacts.objects.get(owner=contact_owner)
            new_contact.contacts.add(cc)

            print('c', cc)
            return HttpResponseRedirect(reverse('messager:contacts'))

    comment = 'Добавление контакта пользователем {}'.format(contact_owner_name)
    content = {'form': contacts_form, 'comment': comment}
    return render(request, 'add_contact.html', content)


@login_required()
def send(request, recipient_id):
    '''Отправка сообщения получателю'''
    form = Talk(data=request.POST)
    print(request.POST)
    # print(recipient_id)
    sender = request.user
    recipient = User.objects.get(id=recipient_id)
    print('view.send: {} (sender) {} (recipient)'.format(sender.username, recipient.username))

##############################################################
    try:
        m_text = form.data['text']
        print(m_text)
    except KeyError:
        m_text = 0
        print('Сообщение в форме отсутствует...')

    # передаем новое сообщение, если имеется
    if m_text:
        m = Message(sender, recipient, m_text)
        list_m.send(m)
        form.clean_text()
###############################################################

    # формируем список из сообщений диалога двух пользователей
    l_c = list_m.correspondence(sender, recipient)
    print(l_c)
    for l in l_c:
        print('{} от {} для {}: {}, {}'.format(l.date_time, l.sender.username, l.recipient.username, l.text, l.is_read))

    # форматируем в список строк для вывода в шаблон
    comment = ['{} от {} для {}: {}'.format(l.date_time, l.sender.username, l.recipient.username, l.text) for l in
               l_c]

    if request.is_ajax():
        print('send - ajax request')
        content1 = {'comment': comment}
        result = render_to_string('messager/templates/inc_talk.html', content1)
        return JsonResponse({'result': result})
    else:
        print('not ajax request')
        content = {'form': form, 'comment': comment, 'sender': sender, 'recipient': recipient,
                   'recipient_id': recipient_id}
        return render(request, 'talk.html', content)

