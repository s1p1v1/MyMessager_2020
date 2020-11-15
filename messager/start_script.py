#!/usr/bin/env python3

import datetime

#   User dialog objects (объекты диалога пользователей)
# Скрипт запускается автоматом вместе с сервером...

class User:
    # Пользователь (только для проверки работоспособности)
    def __init__(self, name):
        self.name = name

class Message:
    # Объект сообщения text от пользователя sender для пользователя recipient
    def __init__(self, sender, recipient, text):
        # пользователь отправитель
        self.sender = sender
        # пользователь получатель
        self.recipient = recipient
        # текст сообщения
        self.text = text
        # дата и время отправления
        self.date_time = datetime.datetime.now()
        # признак прочтения
        self.is_read = False

    def read(self):
        # прочитать сообщение
        self.is_read = True

class Messages:
    # Список всех сообщений всех пользователей
    def __init__(self):
        self.list_messages = []
        print('Создание списка сообщений')

    def send(self, message):
        # отправка сообщения
        self.list_messages.append(message)
        print('Пользователем {} отправлено сообщение пользователю {}'.format(message.sender.username, message.recipient.username))
        # все новые сообщения от данного отправителя объявляем прочитанными
        for m in self.list_messages:
            #print(m.recipient.username, m.is_read)
            if message.recipient == m.sender and message.sender == m.recipient:
                if m.is_read == False:
                    m.read()

    '''
    def read(self, sender, recipient):
        # чтение сообщения
        f = False  # сообщение отсутствует
        print('зашли в read')
        for m in self.list_messages:
            print(m.recipient.username, m.is_read)

            if recipient == m.recipient and sender == m.sender:
                if m.is_read == False:
                    m.read()
                    f = True
                print('Сообщение прочитано пользователем {} - {}'.format(m.recipient.username, m.is_read))
                return m

        if not f:
            print('Новых сообщений для пользователя {} нет!'.format(recipient.username))
    '''

    def correspondence(self, sender, recipient):
        # список сообщений текущего диалога между sender и recipient
        list_messages = []

        for m in self.list_messages:
            if (recipient == m.recipient and sender == m.sender) or (recipient == m.sender and sender == m.recipient):
                list_messages.append(m)
                #m.read()    # сообщение не попадает в список новых...

        return list_messages

    def reception(self, recipient):
        # список имен отправителей новых сообщений для пользователя (recipient)
        list_senders_messages = []
        print('полный список сообщений', self.list_messages)
        for m in self.list_messages:
            if recipient == m.recipient and m.is_read == False:
                print('Пользователь {} получил сообщение от {}'.format(m.recipient.username, m.sender.username))
                list_senders_messages.append(m.sender.username)
                #m.read()   # в цикле ajax опроса список новых сообщений слишком быстро обнуляется...

        return list_senders_messages


def main():
    user1 = User('peter')
    user2 = User('nico')
    m_db = Messages()
    t1 = 'Привет, Коля!'
    m1 = Message(user1, user2, t1)
    m_db.send(m1)
    m_db.read(user2)
    print(m1.date_time, m1.text)



if __name__ == "__main__":
    main()
