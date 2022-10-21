from django.urls import path, re_path #re_pach - позволяет задавать урлы с использованием регулярных вырожений
from .views import *

urlpatterns = [
    path('', index, name='home'), # name='home' - это именованный параметр для внутреннего обращения в коде (например для редиректа)
    path('cats/<int:cat_id>/', categories), # числовой параметр <тип:имя_параметра>, в конце ставим '/'
    re_path(r'archive/(?P<year>[0-9]{4})/', archive),
]