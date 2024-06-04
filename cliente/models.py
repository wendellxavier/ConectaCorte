from django.db import models
from django.contrib.auth.models import User
from cabeleleiro.models import DatasAbertas

class Atendimento(models.Model):
    status_choices = (
        ('A', 'Agendado'),
        ('F', 'Finalizado'),
        ('C', 'Cancelado'),
        ('I', 'Inicializado')
    )
    cliente = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_aberta = models.ForeignKey(DatasAbertas, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=status_choices, default='A')
    link = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.cliente.username
