from django.db import models
from comun.models import Pais, Estado, Cidade

class Clube(models.Model):
    nome = models.CharField(max_length=120)
    cores = models.CharField(max_length=80, blank=True, null=True)
    ano_fundacao = models.PositiveIntegerField(default=0)
    tem_mundial = models.BooleanField(default=False)
    escudo = models.ImageField(upload_to='clubes', null=True)

    cidade = models.ForeignKey(
        Cidade, on_delete=models.CASCADE, related_name='clubes', null=True)

    def __str__(self):
        return self.nome
    

class JOgador(models.Model):

    posicao_choices = (
        ('AT', 'Atacante'),
        ('ZG', 'Zagueiro'),
    )

    sexo_choices = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )


    nome = models.CharField(max_length=120)
    foto = models.ImageField()
    posicao = models.CharField(max_length=120, choices=posicao_choices)

