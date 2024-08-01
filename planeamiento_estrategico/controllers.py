from flask import request, jsonify
from app import app, db
from models import Estrategia
from repositories import EstrategiaRepository

repo = EstrategiaRepository()

@app.route('/estrategias', methods=['POST'])
def create_estrategia():
    data = request.get_json()
    estrategia = Estrategia(nombre=data['nombre'], descripcion=data['descripcion'])
    repo.adicionar(estrategia)
    return jsonify({"message": "Estrategia creada"}), 201

@app.route('/estrategias/<int:id>', methods=['GET'])
def read_estrategia(id):
    estrategia = repo.buscar(id)
    if estrategia:
        return jsonify({"id": estrategia.id, "nombre": estrategia.nombre, "descripcion": estrategia.descripcion}), 200
    return jsonify({"message": "Estrategia no encontrada"}), 404

@app.route('/estrategias/<int:id>', methods=['DELETE'])
def delete_estrategia(id):
    repo.eliminar(id)
    return jsonify({"message": "Estrategia eliminada"}), 204

@app.route('/estrategias/<int:id>', methods=['PUT'])
def update_estrategia(id):
    data = request.get_json()
    estrategia = repo.buscar(id)
    if estrategia:
        estrategia.nombre = data['nombre']
        estrategia.descripcion = data['descripcion']
        repo.actualizar(estrategia)
        return jsonify({"message": "Estrategia actualizada"}), 200
    return jsonify({"message": "Estrategia no encontrada"}), 404
