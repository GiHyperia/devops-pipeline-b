"""Tests unitarios: prueban la lógica de negocio de forma aislada."""

import pytest

from app.saludos import idiomas_disponibles, saludar


def test_saludo_por_defecto():
    assert saludar() == "Hola, mundo!"


@pytest.mark.parametrize(
    "idioma, esperado",
    [
        ("es", "Hola, Ana!"),
        ("en", "Hello, Ana!"),
        ("pt", "Olá, Ana!"),
        ("fr", "Bonjour, Ana!"),
        ("it", "Ciao, Ana!"),
    ],
)
def test_saludo_en_cada_idioma(idioma, esperado):
    assert saludar("Ana", idioma) == esperado


def test_nombre_vacio_usa_mundo():
    assert saludar("   ") == "Hola, mundo!"


def test_idioma_no_soportado_lanza_error():
    with pytest.raises(ValueError):
        saludar("Ana", "de")


def test_idiomas_disponibles():
    assert idiomas_disponibles() == ["en", "es", "fr", "it", "pt"]
