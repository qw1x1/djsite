from django.db import models
from django.urls import reverse

class Women(models.Model):
    # id - уже есть в базовом классе
    title = models.CharField(max_length=255, verbose_name= 'Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL") # unique=True - не будет повторок
    content = models.TextField(blank=True, verbose_name= 'Текст')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name= 'Фото') # Для работы со статическими данными нужен python -m pip install Pillow
    time_create = models.DateTimeField(auto_now_add=True, verbose_name= 'Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name= 'Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name= 'Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null= True, verbose_name= 'Категория') # Отношение многие к одному (у нескольких женьщины может быть одинаеовая категория)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['time_create', 'title']# Сортировка по умоланию как на сайте так и в админке

class Category(models.Model):
    name = models.CharField(max_length=100, db_index = True, verbose_name= 'Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
    
    class Meta:
        verbose_name = 'Категории' 
        verbose_name_plural = 'Категории'
        ordering = ['id']# Сортировка по умоланию как на сайте так и в админке

# class User(models.Model):
#     name = models.CharField(max_length=100, db_index = True, verbose_name= 'Имя')
#     login = models.CharField(max_length=32, unique=True, verbose_name= 'Логин')
#     password = models.CharField(max_length=32, verbose_name= 'Пароль')
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
#     photo = models.ImageField(upload_to="photos/users/%Y/%m/%d/", verbose_name= 'Фото')
#     time_create = models.DateTimeField(auto_now_add=True, verbose_name= 'Дата регистрации')

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('show_user', kwargs={'user_slug': self.slug})

#     class Meta:
#         verbose_name = 'Пользователи' 
#         verbose_name_plural = 'Пользователи'
#         ordering = ['time_create']# Сортировка по умоланию как на сайте так и в админке