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


def login_user(request):
    context = {
     'title': 'Войти',
    }
    return render(request, 'women/input.htm', context=context)

def about(request):
    return render(request, 'women/about.htm', {'title': 'О сайте'})

def contact(request):
    return HttpResponse('Контакты')

# Обработчик при ошибки 404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h2>Page not found 404 - Страница не найдена 404</h2>')

