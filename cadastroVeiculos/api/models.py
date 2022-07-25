from django.db import models


class Veiculos(models.Model):
    veiculo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    ano = models.IntegerField()
    descricao = models.TextField()
    vendido = models.BooleanField()

    def __str__(self):
        return self.veiculo
