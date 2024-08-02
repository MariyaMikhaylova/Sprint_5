import random


def generate_login(length):
    login = ""
    for i in range(length):
        login = login + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return f'{login}@yandex.ru'


def generate_password(length):
    password = ""
    for i in range(length):
        password = password + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return password
