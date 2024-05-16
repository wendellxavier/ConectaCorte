from django.db import models

class Especialidades(models.Model):
    especialidade = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'
    
    def __str__(self):
        return self.especialidade
    
class DadosCabeleleiro(models.Model):
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField(max_length=100)
    anos_de_experiencia = models.IntegerField()
    rg = models.ImageField()
    