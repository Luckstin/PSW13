from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentorados, name='mentorados'),
    path('reunioes/', views.reunioes, name='reunioes'),
    path('escolher_dia/', views.escolher_dia, name='escolher_dia'),
    path('auth/', views.auth, name="auth_mentorado"),
    path('agendar_reuniao/', views.agendar_reuniao, name='agendar_reuniao'),
    path('tarefa/<int:id>', views.tarefa, name='tarefa'),
    path('tarefa_alterar/<int:id>', views.tarefa_alterar, name="tarefa_alterar"),
]