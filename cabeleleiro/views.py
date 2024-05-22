from django.shortcuts import render
from .models import Especialidades, TipoCabelos
from django.http import HttpResponse

def cadastro_cabeleleiro(request):
    if request.method == "GET":
        especialidades = Especialidades.objects.all()
        tipoCabelos = TipoCabelos.objects.all()
        return render (request, 'cadastro_cabeleleiro.html', {'especialidades': especialidades, 'tipoCabelos': tipoCabelos})
    elif request.method == "POST":
        return HttpResponse('teste deu certo')
        
        
