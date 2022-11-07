from django.urls import path, re_path #re_pach - позволяет задавать урлы с использованием регулярных вырожений
from .views import *

urlpatterns = [
    path('', index, name='home'), # name='home' - это именованный параметр для внутреннего обращения в коде (например для редиректа) 
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name='category'),
    # path('user_create/', create_user, name='create_user'),
    # path('user/<slug:user_slug>/', show_user, name='show_user'),
    path('login/', login_user, name='login_user'),
]