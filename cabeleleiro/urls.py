from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_cabeleleiro', views.cadastro_cabeleleiro, name="cadastro_cabeleleiro"),
]
