"""Lógica de negocio: saludos en varios idiomas."""

SALUDOS = {
    "es": "Hola",
    "en": "Hello",
    "pt": "Olá",
    "fr": "Bonjour",
}


def idiomas_disponibles():
    """Devuelve la lista de idiomas soportados, ordenada."""
    return sorted(SALUDOS)


def saludar(nombre="mundo", idioma="es"):
    """Devuelve un saludo personalizado en el idioma indicado."""
    if idioma not in SALUDOS:
        raise ValueError(f"Idioma no soportado: {idioma}")
    nombre = (nombre or "").strip() or "mundo"
    return f"{SALUDOS[idioma]}, {nombre}!"
