from django.urls import path, re_path #re_pach - позволяет задавать урлы с использованием регулярных вырожений
from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'), # name='home' - это именованный параметр для внутреннего обращения в коде (например для редиректа) 
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    path('user_create/', Register_user.as_view(), name='create_user'),
    path('login/', LoginUuser.as_view(), name='login_user'),
    path('exit/', logout_user, name='logout_user')
    # path('user/<slug:user_slug>/', show_user, name='show_user'),
]