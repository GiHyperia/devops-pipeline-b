"""API web (Flask) que expone la lógica de saludos."""

from flask import Flask, jsonify, request

from app.saludos import idiomas_disponibles, saludar

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/idiomas")
def idiomas():
    return jsonify(idiomas=idiomas_disponibles())


@app.get("/saludo")
def saludo():
    nombre = request.args.get("nombre", "mundo")
    idioma = request.args.get("idioma", "es")
    try:
        return jsonify(saludo=saludar(nombre, idioma))
    except ValueError as error:
        return jsonify(error=str(error)), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
