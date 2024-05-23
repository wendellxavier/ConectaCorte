from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_cabeleleiro', views.cadastro_cabeleleiro, name="cadastro_cabeleleiro"),
    path('abrir_horario', views.abrir_horario, name="abrir_horario"),
]
