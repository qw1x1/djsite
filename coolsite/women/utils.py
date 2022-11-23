from .models import *
from django.db.models import Count
from django.core.cache import cache


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]

class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        # API низкоуровневого кеширования
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('women'))
            cache.set('cats', cats, 60)
 
        user_menu = menu.copy()
        # Т.к DataMixin связан с запросом у него есть доступ к request
        if not self.request.user.is_authenticated:
        # У объекта user есть св-во is_authenticated (авторизован или нет пользователь)
            user_menu.pop(1) # удаляем пункт меню для не авторизованных пользователей {'title': "Добавить статью", 'url_name': 'add_page'},

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
 
        return context