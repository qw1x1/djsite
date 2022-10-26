from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('name/<str:name>/', name),
]