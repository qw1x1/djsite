from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

def name(request, name):
    names ={'vasa': 'Vladimir', 'lox': 'Oleksej', 'vlad': 'Vladislav'}
    if str(name) in names:
        return HttpResponse(f'<h1>Ваше полное имя</h1> <h2>{names.get(str(name))}</h2>')
    else:
        return HttpResponse(f'<h1>Такого имени нет в базе</h1>')

