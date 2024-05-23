from django.shortcuts import render, redirect
from .models import Especialidades, TipoCabelos, DadosCabeleleiro
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants

def cadastro_cabeleleiro(request):
    
    dc = DadosCabeleleiro.objects.filter(user=request.user)
    if dc.exists():
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