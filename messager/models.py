from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Sender(models.Model):
    '''Участник'''
    participant = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Участник')
    online = models.BooleanField(default=False)

class Contacts(models.Model):
    '''Контакты'''
    sender = models.ManyToManyField(Sender, blank=True, related_name='contacts', verbose_name='Контактер')
    '''Владелец контактов'''
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Владелец контактов')

class Messages(models.Model):
    '''Сообщения пользователей'''
    recipient = models.ManyToManyField(Sender, blank=True, related_name='messages', verbose_name='Получатель')
    sender = models.OneToOneField(User, unique=False, default=1000, on_delete=models.CASCADE, verbose_name='Отправитель')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата/Время')
    text = models.TextField(verbose_name='Сообщение')
    new = models.BooleanField(default=True)  # не прочитано
