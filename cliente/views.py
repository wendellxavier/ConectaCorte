from django.shortcuts import render, redirect
from cabeleleiro.models import DadosCabeleleiro, Especialidades, TipoCabelos, DatasAbertas
from datetime import datetime
from .models import Atendimento
from django.contrib import messages
from django.contrib.messages import constants


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


def escolher_horario(request, id_dados_cabeleleiros):
    if request.method == "GET":
        cabeleleiro = DadosCabeleleiro.objects.get(id=id_dados_cabeleleiros)
        datas_abertas = DatasAbertas.objects.filter(user=cabeleleiro.user).filter(data__gte=datetime.now()).filter(agendado=False)
        return render(request,'escolher_horario.html', {'cabeleleiro': cabeleleiro, 'datas_abertas': datas_abertas})

def agendar_horario(request, id_data_aberta):
    if request.method == "GET":
        data_aberta = DatasAbertas.objects.get(id=id_data_aberta)
        
        horario_agendado = Atendimento(cliente=request.user, data_aberta=data_aberta)
        
        horario_agendado.save()
        
        data_aberta.agendado = True
        data_aberta.save()
        messages.add_message(request, constants.SUCCESS, 'Atendimento agendado com sucesso')
        return redirect('/cliente/meus_atendimentos')