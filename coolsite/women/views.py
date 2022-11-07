from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import * # Импортируем модели
from .forms import * # Импортируем формы

def index(request):
    posts = Women.objects.order_by('title') # Загружаем таблицу из бд

    context = {
     'posts': posts,
     'title': 'Главная страница',
     'cat_selected': 0,
    }
    return render(request, 'women/index.htm', context=context) # context - это имя именованного параметра

def show_post(request, post_slug):   
    posts = get_object_or_404(Women, slug=post_slug) # Загружаем нужную запись из бд

    context = {
     'posts' : posts,
     'title': posts.title,
     'cat_selected': posts.cat_id,
    } 
    return render(request, 'women/post.htm', context=context)

def show_category(request, cat_slug):
    categ = Category.objects.get(slug=cat_slug)
    posts = Women.objects.filter(cat_id=categ.pk) # Загружаем нужную запись из бд

    if len(posts) == 0:
        raise Http404()

    context = {
     'posts': posts,
     'title': f'Категория {categ.name}',
     'cat_selected': categ.pk,
    }
    return render(request, 'women/index.htm', context=context)

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES) # request.FILES - список содержащий файлы загруженные пользователем
        if form.is_valid():
            #print(form.cleaned_data)
            form.save() # Сохраняем данные 
            return redirect('home')
    else:
        form = AddPostForm()
        
    context = {
     'form': form,
     'title': 'Добавление статьи',
    }
    return render(request, 'women/addpage.htm', context=context)


# РАБОТА С ПОЛЬЗОВАТЕЛЯМИ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# def show_user(request, user_slug):
#     users = Women.objects.get_object_or_404(slug=user_slug)

#     context = {
#      'posts': users,
#      'title': f'Страница пользователя: {users.name}',
#     }
#     return render(request, 'women/user.htm', context=context)

# def create_user(request):
#     if request.method == 'POST':
#         form = Input(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save() # Сохраняем данные 
#             return redirect('show_user')
#     else:
#         form = Input()

#     context = {
#      'form' : form,
#      'title': 'Войти',
#     }
#     return render(request, 'women/input.htm', context=context)

def login_user(request):
    # if request.method == 'POST':
    #     form = Input(request.POST) # request.FILES - список содержащий файлы загруженные пользователем
    #     if form.is_valid():


    #         return redirect('home')
    # else:
    #     form = Input()

    context = {
    #  'form' : form,
     'title': 'Войти',
    }
    return render(request, 'women/input.htm', context=context)
# РАБОТА С ПОЛЬЗОВАТЕЛЯМИ----------------------------------------------------------------------------------------------------------------------
def about(request):
    return render(request, 'women/about.htm', {'title': 'О сайте'})

def contact(request):
    return HttpResponse('Контакты')

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

