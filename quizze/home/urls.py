
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('api/get_quizze',views.get_quiz,name='get_quizze')
]