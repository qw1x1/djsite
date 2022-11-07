from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import * # Импортируем модели
from .forms import * # Импортируем формы
from django.views.generic import ListView, DetailView, CreateView # Импортируем классы-представления
# ListView - отображает список записей модели 
# DetailViev - отображает конкретную запись модели 
# CreateView - для работы с формами

# Главная страница
class WomenHome(ListView):
    model = Women # атрибут model ссылается на модель 
    template_name = 'women/index.htm' # Передаём шаблон в представление
    # ListView - автоматически формирует колекцию object_list, с которой можно работать в teamplate, либо можем переопределить это имя 
    context_object_name = 'posts' # теперь бкдем работать с колекцией по имени posts, имя используемое в templates
    # extra_context = {'title': 'Главная страница'} С помощю данной переменной можно передавать статические данные (но не динамические)
    # Для передачи динамических данных переопределяем метод get_context_data
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) # Берем ранее созданый контекст, чтобы не потерять его 
        context['title'] = 'Главная страница' # добавляем данные в контекст (можно и статичесткие, но можно и список, например меню)
        context['cat_selected'] = 0 # Передаём параметр для отбражения активной вкладки меню_категорий
        return context
    # Для выборки данных оперделим метод get_queryset
    def get_queryset(self):
        return Women.objects.filter(is_published=True) # Вернёт только опубликованные записи

# Страница отдельной категории
class WomenCategory(ListView):
    model = Women 
    template_name = 'women/index.htm'
    context_object_name = 'posts'
    allow_empty = False # генерирует оштбку если нет записей, get_context_data - метод не будет обрабатываться

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) # Сохраняем уже сформированный контекст
        # Через контекст обращаемся к posts, берём 1-ю запись и берем категорию, при этом в модели сработаем метод __str__ и вернём name
        context['title'] = 'Категория - ' + str(context['posts'][0].cat) 
        context['cat_selected'] = context['posts'][0].cat_id #
        return context
 
    def get_queryset(self):
        # self.kwargs - через данный словать можем получить все переменные нашего маршрута
        # Для выборки данных из связанной модели Category используя cat__slug можем обрятиться к конкретоной категории и просмотреть ее поле (slug, и т.п)
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True) 

# Страница отдельного поста
class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.htm'
    slug_url_kwarg = 'post_slug' # Принудительно переопреденяем имя переменной из urls, (pk_url_kwarg = 'имя из urls' - для id)
    context_object_name = 'post' # Имя переменной для templates

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['cat_selected'] = context['post'].cat_id 
        return context

# Страница добавления поста
class AddPage(CreateView):
    form_class = AddPostForm # Указываем имя класса формы
    template_name = 'women/addpage.htm'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES) # request.FILES - список содержащий файлы загруженные пользователем
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save() # Сохраняем данные 
#             return redirect('home')
#     else:
#         form = AddPostForm()
        
#     context = {
#      'form': form,
#      'title': 'Добавление статьи',
#     }
#     return render(request, 'women/addpage.htm', context=context)


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

