from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import * # Импортируем модели

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        {'title': 'asd'}
]

def index(request):
    category = Category.objects.all()
    posts = Women.objects.order_by('title') # Загружаем таблицу из бд
    context = {
     'posts': posts,
     'cats': category,
     'menu': menu, 
     'title': 'Главная страница',
     'cat_selected': 0,
    }
    return render(request, 'women/index.htm', context=context) # context - это имя именованного параметра

def about(request):
    return render(request, 'women/about.htm', {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    return HttpResponse('Добавить статью')

def contact(request):
    return HttpResponse('Контакты')

def login(request):
    return HttpResponse('Войти')

def show_post(request, post_id):   
    posts = Women.objects.get(pk=post_id) # Загружаем нужную запись из бд
    context = {
     'posts' : posts,
     'menu': menu, 
     'title': posts.title,
    } 
    return render(request, 'women/post.htm', context=context)

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id) # Загружаем нужную запись из бд
    category = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
     'posts': posts,
     'cats': category,
     'menu': menu, 
     'title': 'Отображение по рубрикам',
     'cat_selected': cat_id,
    }
    return render(request, 'women/index.htm', context=context)

# Обработчик при ошибки 404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Page not found 404 - Страница не найдена 404</h2>')

# def categories(request, cat_id): # указываем числовой параметр как в урле
# # request.GET #->http://127.0.0.1:8000/cats/22/?key1=value1&key2=value2
# # request.GET - получает словарь который хранит все параметры указаные в ссылке <QueryDict: {'key1': ['value1'], 'key2': ['value2']}>
#     if request.GET:
#         print(request.GET)
#     if int(cat_id) < 7:
#         raise Http404()
#     return HttpResponse(f'<h1>Статьи по категориям</h1><h2>{cat_id}</h2>')
# # POST - запрос, обычно работает совместно с формами, при передаче данных от пользователя
# # if request.POST:
# # print(request.POST)

# def archive(request, year):
#     if int(year) < 2020:
#         # Редирект на другую стр    
#         # return redirect('home') #-> 302
#         return redirect('home', permanent=True) #-> При permanent=True, будет 301 ошибка
#     return HttpResponse(f'<title>Архив</title><h1>Архив по годам</h1><p>{year}</p>')

# Обработчик при ошибки 500
# def ServerError(request, exceptoin):
#     return HttpResponseNotFound('<h1>Страница не найдена</h1>')

