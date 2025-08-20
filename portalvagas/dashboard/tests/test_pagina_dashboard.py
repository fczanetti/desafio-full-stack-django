import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_deve_carregar_pagina_dashboard(client):
    response = client.get(reverse('dashboard:dashboard'))
    assert response.status_code == 200
