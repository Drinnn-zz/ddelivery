from django.db import models


class MalhaFerroviaria(models.Model):
    ponto_origem: models.CharField(max_length=2)
    ponto_destino: models.CharField(max_length=2)


class Mapa(models.Model):
    nome: models.CharField(max_length=100)
    id_malha_ferrov: models.ForeignKey(
        MalhaFerroviaria, on_delete=models.CASCADE)
