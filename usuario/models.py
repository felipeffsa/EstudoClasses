from django.db import models

# Create your models here.

class Profissao(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nome

class Pessoas(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50)
    idade = models.FloatField(default =5.3)
    profissao = models.ForeignKey(Profissao,on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return self.nome 