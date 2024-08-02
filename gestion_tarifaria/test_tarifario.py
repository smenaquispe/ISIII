import pytest
from flask import Flask, jsonify, request
from flask.testing import FlaskClient

# Define la función create_app aquí
def create_app() -> Flask:
    app = Flask(__name__)

    @app.route('/tarifarios/crear', methods=['POST'])
    def crear_tarifario():
        data = request.json
        # Simula la creación de una tarifa
        return jsonify({'message': 'Tarifa creada', 'id': '12345'}), 201

    @app.route('/tarifarios/<id>/aprobar', methods=['POST'])
    def aprobar_tarifario(id):
        # Simula la aprobación de una tarifa
        return jsonify({'message': 'Tarifa aprobada'}), 200

    return app

@pytest.fixture
def app() -> Flask:
    app = create_app()
    yield app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()

def test_crear_tarifario(client: FlaskClient):
    response = client.post('/tarifarios/crear', json={
        'nombre': 'Tarifa Test',
        'descripcion': 'Descripción de prueba',
        'importe': 100.0
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Tarifa creada'

def test_aprobar_tarifario(client: FlaskClient):
    # Primero crea un tarifario
    response = client.post('/tarifarios/crear', json={
        'nombre': 'Tarifa Test',
        'descripcion': 'Descripción de prueba',
        'importe': 100.0
    })
    assert response.status_code == 201
    tarifario_id = response.json.get('id')

    # Ahora aprueba el tarifario creado
    response = client.post(f'/tarifarios/{tarifario_id}/aprobar')
    assert response.status_code == 200
    assert response.json['message'] == 'Tarifa aprobada'

