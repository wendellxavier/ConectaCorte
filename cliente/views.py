from django.shortcuts import render
from cabeleleiro.models import DadosCabeleleiro


def home(request):
    if request.method == "GET":
        cabeleleiros = DadosCabeleleiro.objects.all()
        return render(request, 'home.html', {'cabeleleiros': cabeleleiros})
