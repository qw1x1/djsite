from django import template
from women.models import *

register = template.Library()

# Простой тег возвращает коллекцию данных "queriset"
# Простой тег. в декораторе укажем альтеронативное имя для нашего тега, вместо имени функции
@register.simple_tag(name='getcats')
def get_categories(): # В шаблоне для использования тега(данных) обращаеся по имени функции
    return Category.objects.all()

# Включаещий тег формирует фрагметн html страницы
@register.inclusion_tag('women/list_categories.htm')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
 
    return {"cats": cats, "cat_selected": cat_selected}# Данные принимает list_categories.htm

