# Proyecto T3 - Sistema de Gestion de Servicios Academicos

Proyecto demostrativo para practicar pruebas automatizadas con Pytest, integración continua con GitHub Actions y ejecución con Docker.

## Requisitos
- Python 3.12 o superior
- Docker Desktop
- Git (para publicar el repositorio)

## Ejecutar localmente en Windows PowerShell

Desde la carpeta del proyecto:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -v
python app.py
```

Abrir:
- http://localhost:5000/
- http://localhost:5000/estudiantes
- http://localhost:5000/salud

## Construir y ejecutar con Docker

```powershell
docker build -t sistema-academico-t3 .
docker run -d --name sistema-academico -p 5000:5000 sistema-academico-t3
docker ps
```

Para detener y eliminar el contenedor:

```powershell
docker stop sistema-academico
docker rm sistema-academico
```

También se puede ejecutar con Docker Compose:

```powershell
docker compose up -d --build
docker compose ps
```

Para detenerlo:

```powershell
docker compose down
```

## GitHub Actions

El workflow está en `.github/workflows/ci-cd.yml`. Se ejecuta automáticamente al hacer `push` o abrir un `pull_request` hacia `main`. Ejecuta las pruebas, construye la imagen Docker y verifica el endpoint `/salud`.

## Nota
Este es un proyecto académico de demostración. Los nombres y datos de estudiantes son ficticios.
