from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Импортформы добавления нового пользователя
from django.contrib.auth.models import User


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

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))