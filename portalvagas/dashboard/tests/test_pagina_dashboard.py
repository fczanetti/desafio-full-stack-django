from django.urls import reverse


def test_deve_carregar_pagina_dashboard(client):
    response = client.get(reverse('dashboard:dashboard'))
    assert response.status_code == 200
