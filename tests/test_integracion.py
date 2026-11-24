"""Tests de integración: prueban la API completa a través de HTTP."""

import pytest

from app.main import app


@pytest.fixture
def cliente():
    app.config["TESTING"] = True
    return app.test_client()


def test_health(cliente):
    respuesta = cliente.get("/health")
    assert respuesta.status_code == 200
    assert respuesta.get_json() == {"status": "ok"}


def test_idiomas(cliente):
    respuesta = cliente.get("/idiomas")
    assert respuesta.status_code == 200
    assert "es" in respuesta.get_json()["idiomas"]


def test_saludo_con_parametros(cliente):
    respuesta = cliente.get("/saludo?nombre=Giovana&idioma=pt")
    assert respuesta.status_code == 200
    assert respuesta.get_json() == {"saludo": "Olá, Giovana!"}


def test_saludo_idioma_invalido_devuelve_400(cliente):
    respuesta = cliente.get("/saludo?idioma=xx")
    assert respuesta.status_code == 400
    assert "error" in respuesta.get_json()
