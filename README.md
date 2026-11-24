# devops-pipeline-b

API de saludos en Flask con un pipeline DevOps completo.

## Endpoints
- `GET /health` → estado del servicio
- `GET /idiomas` → idiomas disponibles
- `GET /saludo?nombre=Ana&idioma=en` → saludo personalizado

## Ejecutar en local
```bash
python -m venv venv
venv\Scripts\activate          # Windows  (macOS/Linux: source venv/bin/activate)
pip install -r requirements-dev.txt
flake8 --statistics
bandit -r app
pytest -v --cov=app
python -m app.main             # http://127.0.0.1:5000/health
```

## Docker
```bash
docker build -t saludos .
docker run -p 5000:5000 saludos
```

## Pipelines
- **CircleCI** (`.circleci/config.yml`): lint, seguridad y tests con cobertura.
- **GitHub Actions** (`.github/workflows/ci-cd.yml`): CI en Python 3.11–3.13 y CD que
  construye, prueba y publica la imagen Docker en GitHub Packages.
- **Dependabot** (`.github/dependabot.yml`): actualización automática de dependencias.
