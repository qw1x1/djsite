from django.urls import path, re_path #re_pach - позволяет задавать урлы с использованием регулярных вырожений
from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'), # name='home' - это именованный параметр для внутреннего обращения в коде (например для редиректа) 
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    # path('user_create/', create_user, name='create_user'),
    # path('user/<slug:user_slug>/', show_user, name='show_user'),
    path('login/', login_user, name='login_user'),
]