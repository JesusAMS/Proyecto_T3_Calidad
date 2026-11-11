import pytest
from app import app


@pytest.fixture
def cliente():
    app.config["TESTING"] = True
    with app.test_client() as cliente:
        yield cliente


def test_inicio(cliente):
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert respuesta.json["estado"] == "Funcionando correctamente"


def test_estudiantes(cliente):
    respuesta = cliente.get("/estudiantes")
    assert respuesta.status_code == 200
    assert len(respuesta.json["estudiantes"]) == 2


def test_salud(cliente):
    respuesta = cliente.get("/salud")
    assert respuesta.status_code == 200
    assert respuesta.json["estado"] == "OK"
