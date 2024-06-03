from django.shortcuts import render
from cabeleleiro.models import DadosCabeleleiro, Especialidades, TipoCabelos


def home(request):
    if request.method == "GET":
        cabeleleiro_filtrar = request.GET.get('cabeleleiro')
        especialidade_filtrar = request.GET.getlist('especialidades')
        tipoCabelos_filtrar = request.GET.getlist('tiposCabelos')
        cabeleleiros = DadosCabeleleiro.objects.all()
        
        if cabeleleiro_filtrar:
            cabeleleiros = cabeleleiros.filter(nome__icontains=cabeleleiro_filtrar)
            
        if especialidade_filtrar:
            cabeleleiros = cabeleleiros.filter(especialidade_id__in=especialidade_filtrar)
        
        especialidades = Especialidades.objects.all()
        tiposCabelos = TipoCabelos.objects.all()
        return render(request, 'home.html', {'cabeleleiros': cabeleleiros, 'especialidades': especialidades, 'tiposCabelos': tiposCabelos})
