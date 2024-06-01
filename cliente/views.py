from django.shortcuts import render
from cabeleleiro.models import DadosCabeleleiro, Especialidades, TipoCabelos


def home(request):
    if request.method == "GET":
        cabeleleiros = DadosCabeleleiro.objects.all()
        especialidades = Especialidades.objects.all()
        tiposCabelos = TipoCabelos.objects.all()
        return render(request, 'home.html', {'cabeleleiros': cabeleleiros, 'especialidades': especialidades, 'tiposCabelos': tiposCabelos})
