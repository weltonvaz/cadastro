from django.db import models


class Enderecos(models.Model):
    rua = models.CharField('Rua', max_length=100)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=100)
    complemento = models.CharField('Complemento', max_length=100)
    cep = models.CharField('CEP', max_length=8)
