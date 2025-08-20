import pytest
from django.urls import reverse
from datetime import date

from model_bakery import baker
from portalvagas.candidatos.models import Candidato
from portalvagas.vagas.models import Vaga, Candidatura


@pytest.mark.django_db
def test_pagina_deve_ser_acessivel(client):
    response = client.get(reverse('vagas:candidatar'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_pagina_de_candidatura_deve_exibir_vagas_abertas(client):
    vaga = baker.make(Vaga, status=Vaga.ABERTA)
    vaga_2 = baker.make(Vaga, status=Vaga.ABERTA)
    response = client.get(reverse('vagas:candidatar'))

    assert vaga.titulo in response.content.decode()
    assert vaga.setor in response.content.decode()
    assert vaga_2.titulo in response.content.decode()
    assert vaga_2.setor in response.content.decode()


@pytest.mark.django_db
def test_pagina_de_candidatura_deve_exibir_apenas_vagas_abertas(client):
    vaga = baker.make(Vaga, status=Vaga.ABERTA)
    vaga_fechada = baker.make(Vaga, status=Vaga.FECHADA)
    response = client.get(reverse('vagas:candidatar'))

    assert vaga.titulo in response.content.decode()
    assert vaga.setor in response.content.decode()

    assert vaga_fechada.titulo not in response.content.decode()
    assert vaga_fechada.setor not in response.content.decode()


@pytest.mark.django_db
def test_deve_registrar_candidatura(client):
    vaga = baker.make(Vaga, status='aberta')

    assert Candidatura.objects.count() == 0
    assert Candidato.objects.count() == 0

    response = client.post(reverse('vagas:candidatar'), data={
        'nome': 'Candidato Teste',
        'email': 'candidato@teste.com',
        'data_nascimento': '2000-01-01',
        'experiencia': 'Experiência Teste',
        'vagas': vaga.id
    })

    assert response.status_code == 302
    assert response.url == reverse('vagas:candidatar')

    assert Candidatura.objects.count() == 1
    assert Candidato.objects.count() == 1

    candidato = Candidato.objects.first()
    assert candidato.nome == 'Candidato Teste'
    assert candidato.email == 'candidato@teste.com'
    assert candidato.data_nascimento == date(2000, 1, 1)
    assert candidato.experiencia == 'Experiência Teste'
    assert candidato.vagas.first() == vaga


@pytest.mark.django_db
def test_nao_deve_registrar_candidatura_de_usuario_para_mesma_vaga_duas_vezes(client):
    vaga = baker.make(Vaga, status='aberta')
    candidato = baker.make(Candidato, nome='Candidato Teste', email='candidato@teste.com')
    baker.make(Candidatura, candidato=candidato, vaga=vaga)

    assert Candidatura.objects.count() == 1

    client.post(reverse('vagas:candidatar'), data={
        'nome': 'Candidato Teste',
        'email': 'candidato@teste.com',
        'data_nascimento': '2000-01-01',
        'experiencia': 'Experiência Teste',
        'vagas': vaga.id
    })

    assert Candidatura.objects.count() == 1
