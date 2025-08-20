from django.db import models

from portalvagas.candidatos.models import Candidato


class Vaga(models.Model):
    ABERTA = "aberta"
    FECHADA = "fechada"

    STATUS_CHOICES = [
        (ABERTA, 'Aberta'),
        (FECHADA, 'Fechada'),
    ]

    titulo = models.CharField(max_length=200)
    setor = models.CharField(max_length=100)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=ABERTA
    )
    data_abertura = models.DateField(auto_now_add=True)
    candidatos = models.ManyToManyField(Candidato, through='Candidatura', related_name='vagas')

    def __str__(self):
        return f"{self.titulo} - {self.setor}"


class Candidatura(models.Model):
    PENDENTE = "pendente"
    APROVADA = "aprovada"
    REJEITADA = "rejeitada"

    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (APROVADA, 'Aprovada'),
        (REJEITADA, 'Rejeitada'),
    ]

    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    status_candidatura = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDENTE)

    class Meta:
        unique_together = ('candidato', 'vaga')

    def __str__(self):
        return f"{self.candidato} - {self.vaga} ({self.status_candidatura})"
