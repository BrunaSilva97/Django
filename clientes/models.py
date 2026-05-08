from django.db import models

# Create your models here.

class Clientes(models.Model):
    nome = models.CharField(max_length=100, null=False)
    cpf = models.CharField(max_length=15, null=False)

def __str__(self):
    return self.nome
