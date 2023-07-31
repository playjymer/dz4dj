# app_lesson_4/views.py

from django.http import HttpResponse

def lesson_4_view(request):
    return HttpResponse("Домашка по 4 занятию")
