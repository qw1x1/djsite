from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import * # Импортируем модели

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):
    posts = Women.objects.order_by('title') # Загружаем таблицу из бд
    return render(request, 'women/index.htm', {'posts' : posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'women/about.htm', {'menu': menu, 'title': 'О сайте'})

def categories(request, cat_id): # указываем числовой параметр как в урле
# request.GET #->http://127.0.0.1:8000/cats/22/?key1=value1&key2=value2
# request.GET - получает словарь который хранит все параметры указаные в ссылке <QueryDict: {'key1': ['value1'], 'key2': ['value2']}>
    if request.GET:
        print(request.GET)
    if int(cat_id) < 7:
        raise Http404()
    return HttpResponse(f'<h1>Статьи по категориям</h1><h2>{cat_id}</h2>')
# POST - запрос, обычно работает совместно с формами, при передаче данных от пользователя
# if request.POST:
# print(request.POST)

def archive(request, year):
    if int(year) < 2020:
        # Редирект на другую стр    
        # return redirect('home') #-> 302
        return redirect('home', permanent=True) #-> При permanent=True, будет 301 ошибка
    return HttpResponse(f'<title>Архив</title><h1>Архив по годам</h1><p>{year}</p>')

# Обработчик при ошибки 404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Page not found 404 - Страница не найдена 404</h2>')

# Обработчик при ошибки 500
# def ServerError(request, exceptoin):
#     return HttpResponseNotFound('<h1>Страница не найдена</h1>')

