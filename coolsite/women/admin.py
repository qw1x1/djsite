from django.contrib import admin
from .models import*

# Класс для админеи
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published', 'cat') #Поля для просмтора 
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content') # Картеж с полями для поиска 
    list_editable = ('is_published',) # Список изменяемых полей 
    list_filter = ('is_published', 'time_create') # Список для фильтрации
    prepopulated_fields = {"slug": ("title", )}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name", )}


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)