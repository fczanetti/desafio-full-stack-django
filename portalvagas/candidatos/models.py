from django.db import models


class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    data_nascimento = models.DateField()
    experiencia = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email
