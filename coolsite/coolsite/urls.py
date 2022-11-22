"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from women.views import pageNotFound #ServerError # оброботчик ошибки 404
from coolsite import settings #
from django.conf.urls.static import static # Для работы со статическими данными

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
]
# handler404 - имя константы в которую передаем ссылку на обработчик ошибки 404
handler404 = pageNotFound
# handler500 - имя константы в которую передаем ссылку на обработчик ошибки 500
# handler500 = ServerError

# При работе с статическими данными моделей, нужно эмулировать работу отладочного сервера, для получения ранее загруженных файлов
# В режиме отладка(settings.DEBUG=True), добавим новый маршрут для статических данных
# При settings.DEBUG=True, добовляем маршрут для статических данных для класса models.Women поля photo
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')), # Добавляем debug_toolbar - в режиме отладки 
    ] + urlpatterns
 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)