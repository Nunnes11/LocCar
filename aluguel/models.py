from django.db import models

class Carro(models.Model):
    modelo = models.CharField("Modelo do carro", max_length=50)
    ano = models.IntegerField("Ano do carro")
    placa = models.CharField("Placa do carro", max_length=10, default='DEFAULT_VALUE')
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.modelo
    
class Cliente(models.Model):
    nome = models.CharField("Nome do cliente", max_length=50)
    email = models.EmailField(default='example@example.com')

    def __str__(self):
        return self.nome

