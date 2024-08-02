from flask import request, jsonify
from flask_restx import Api, Resource, fields
from app import app, db, api, ns
from models import Estrategia
from repositories import EstrategiaRepository

repo = EstrategiaRepository()

estrategia_model = api.model('Estrategia', {
    'nombre': fields.String(required=True, description='The name of the estrategia'),
    'descripcion': fields.String(required=True, description='The description of the estrategia')
})

@ns.route('/')
class EstrategiaList(Resource):
    @ns.doc('create_estrategia')
    @ns.expect(estrategia_model)
    @ns.response(201, 'Estrategia creada')
    def post(self):
        '''Create a new estrategia'''
        data = request.get_json()
        estrategia = Estrategia(nombre=data['nombre'], descripcion=data['descripcion'])
        repo.adicionar(estrategia)
        return {"message": "Estrategia creada"}, 201

@ns.route('/<int:id>')
@ns.response(404, 'Estrategia no encontrada')
class Estrategia(Resource):
    @ns.doc('get_estrategia')
    @ns.marshal_with(estrategia_model)
    def get(self, id):
        '''Fetch a estrategia given its identifier'''
        estrategia = repo.buscar(id)
        if estrategia:
            return estrategia, 200
        api.abort(404, "Estrategia no encontrada")

    @ns.doc('delete_estrategia')
    @ns.response(204, 'Estrategia eliminada')
    def delete(self, id):
        '''Delete a estrategia given its identifier'''
        repo.eliminar(id)
        return {"message": "Estrategia eliminada"}, 204

    @ns.doc('update_estrategia')
    @ns.expect(estrategia_model)
    @ns.response(200, 'Estrategia actualizada')
    def put(self, id):
        '''Update a estrategia given its identifier'''
        data = request.get_json()
        estrategia = repo.buscar(id)
        if estrategia:
            estrategia.nombre = data['nombre']
            estrategia.descripcion = data['descripcion']
            repo.actualizar(estrategia)
            return {"message": "Estrategia actualizada"}, 200
        api.abort(404, "Estrategia no encontrada")


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

api.add_namespace(ns)