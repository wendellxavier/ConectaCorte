from django.shortcuts import render, redirect
from .models import Especialidades, TipoCabelos, DadosCabeleleiro, is_cabeleleiro, DatasAbertas
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime


def cadastro_cabeleleiro(request):
    
    if is_cabeleleiro(request.user):
        messages.add_message(request, constants.WARNING, 'Você já esta cadastrado')
        return redirect('/cabeleleleiro/abrir_horario/')
    
    if request.method == "GET":
        especialidades = Especialidades.objects.all()
        tipoCabelos = TipoCabelos.objects.all()
        return render (request, 'cadastro_cabeleleiro.html', {'especialidades': especialidades, 'tipoCabelos': tipoCabelos})
    elif request.method == "POST":
        if request.user.is_authenticated:
            user_id = request.user.id
            anos_de_experiencia = request.POST.get('anos_de_experiencia')
            nome = request.POST.get('nome')
            cep = request.POST.get('cep')
            rua = request.POST.get('rua')
            bairro = request.POST.get('bairro')
            numero = request.POST.get('numero')
            certificado = request.FILES.get('certificado')
            rg = request.FILES.get('rg')
            foto = request.FILES.get('foto')
            especialidade = request.POST.get('especialidade')
            tipoCabelo = request.POST.get('tipoCabelo')
            descricao = request.POST.get('descricao')
        
   
        dados_cabeleleiro = DadosCabeleleiro(
            user_id=user_id,
            anos_de_experiencia=anos_de_experiencia,
            nome=nome,
            cep=cep,
            rua=rua,
            bairro=bairro,
            numero=numero,
            certificado=certificado,
            rg=rg,
            foto=foto,
            especialidade_id=especialidade,
            tipoCabelo_id=tipoCabelo,
            descricao=descricao
            
            )
        dados_cabeleleiro.save()
        
        messages.add_message(request, constants.SUCCESS, 'Dados salvo com sucesso')
        return redirect('/cabeleleiro/abrir_horario/')
    else:
        return redirect('/cabeleleiro/cadastro_cabeleleiro')
    
    
    
def abrir_horario(request):
    
    if not is_cabeleleiro(request.user):
        messages.add_message(request, constants.WARNING, 'Só cabeleleiro cadastrado podem abrir horários')
        return redirect ('/usuarios/sair/')
    
    if request.method == "GET":
        dados_cabeleleiros = DadosCabeleleiro.objects.get(user=request.user)
        return render(request, 'abrir_horario.html', {'dados_cabeleleiros': dados_cabeleleiros})
    elif request.method == "POST":
        data = request.POST.get('data')
        data_formatada = datetime.strptime(data, "%Y-%m-%dT%H:%M")
        
        if data_formatada <= datetime.now():
            messages.add_message(request, constants.ERROR, 'A data não pode ser anterior que a data atual.')
            return redirect('/cabeleleiro/abrir_horario')
        
        horario_abrir = DatasAbertas(data=data, user=request.user)
        
        horario_abrir.save()
        messages.add_message(request, constants.SUCCESS, 'Horário salvo com sucesso')
        return redirect('/cabeleleiro/abrir_horario/')