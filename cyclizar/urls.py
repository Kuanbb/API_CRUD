from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_usuario, name='get_usuarios'),
    path('user/<str:nick>', views.get_by_nome),
    path('data/', views.controla_usuario, name='cadastra'),
    path('form/', views.form_show),
    path('tabela/', views.tabela_show),
]
