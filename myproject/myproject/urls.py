# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from app_lesson_4.views import lesson_4_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lesson_4/', lesson_4_view, name='lesson_4_view'),  # Добавляем URL для представления lesson_4_view
]
