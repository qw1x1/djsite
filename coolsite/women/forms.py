from django import forms
from django.core.exceptions import ValidationError
from .models import *



# В шаблоне по полям формы можно итерироваться!
class AddPostForm(forms.ModelForm):
    # required = False - делает поле не обязательным
    # initial= True - чекбокс активен по умолчанию
    # Для добовления определённых стилей к полю прописываем атрибут widget
    # title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))
    # slug = forms.SlugField(max_length=255, label="URL")
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Контент")
    # is_published = forms.BooleanField(label="Публикация", initial= True, required = False)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label='Категория не выбрана')

    # Припишем конструктор для 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Обязательно вызываем конструктор базового класса
        self.fields['cat'].empty_label = "Категория не выбрана" # Для поля cat, установим свойство empty_label='ЗНАЧЕНИЕ'

    class Meta:
        model = Women # Связь с моделью
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat'] #Отображаем выбраные поля модели
        # В виджете мы указываем каким полям и какие стили применяем.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    # Для создания ваоидатора пишем метод clean_<имя_поля>
    def clean_title(self): # Валидатор доя поля title
        title = self.cleaned_data['title'] # Получаем данные из колекции cleaned_data (берём title)
        if len(title) < 200:
            raise ValidationError('Длина превышает 200 символов')

        return title

# class Input(forms.Form):
#     # required = False - делает поле не обязательным
#     # initial= True - чекбокс активен по умолчанию
#     # Для добовления определённых стилей к полю прописываем атрибут widget

#     class Meta:
#         model = User # Связь с моделью
#         fields = ['name', 'slug', 'login', 'password', 'photo'] #Отображаем выбраные поля модели
#         # В виджете мы указываем каким полям и какие стили применяем.
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-input'}),
#         }

    # Для создания ваоидатора пишем метод clean_<имя_поля>
    # def clean_login(self): # Валидатор доя поля title
    #     login = self.cleaned_data['login'] # Получаем данные из колекции cleaned_data (берём title)
    #     if len(login) < 200:
    #         raise ValidationError('Данный логин уже занят')

    #     return login