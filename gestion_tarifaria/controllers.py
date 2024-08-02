from flask import request, jsonify
from flask_restx import Api, Resource, fields
from app import app, db, api, ns
from models import Tarifa
from repositories import TarifaRepository

repo = TarifaRepository()

tarifa_model = api.model('Tarifa', {
    'nombre': fields.String(required=True, description='The name of the tarifa'),
    'descripcion': fields.String(required=True, description='The description of the tarifa')
})

@ns.route('/')
class TarifaList(Resource):
    @ns.doc('create_tarifa')
    @ns.expect(tarifa_model)
    @ns.response(201, 'Tarifa creada')
    def post(self):
        '''Create a new tarifa'''
        data = request.get_json()
        tarifa = Tarifa(nombre=data['nombre'], descripcion=data['descripcion'])
        repo.adicionar(tarifa)
        return {"message": "Tarifa creada"}, 201

@ns.route('/<int:id>')
@ns.response(404, 'Tarifa no encontrada')
class Tarifa(Resource):
    @ns.doc('get_tarifa')
    @ns.marshal_with(tarifa_model)
    def get(self, id):
        '''Fetch a tarifa given its identifier'''
        tarifa = repo.buscar(id)
        if tarifa:
            return tarifa, 200
        api.abort(404, "Tarifa no encontrada")

    @ns.doc('delete_tarifa')
    @ns.response(204, 'Tarifa eliminada')
    def delete(self, id):
        '''Delete a tarifa given its identifier'''
        repo.eliminar(id)
        return {"message": "Tarifa eliminada"}, 204

    @ns.doc('update_tarifa')
    @ns.expect(tarifa_model)
    @ns.response(200, 'Tarifa actualizada')
    def put(self, id):
        '''Update a tarifa given its identifier'''
        data = request.get_json()
        tarifa = repo.buscar(id)
        if tarifa:
            tarifa.nombre = data['nombre']
            tarifa.descripcion = data['descripcion']
            repo.actualizar(tarifa)
            return {"message": "Tarifa actualizada"}, 200
        api.abort(404, "Tarifa no encontrada")


@app.route('/tarifas', methods=['POST'])
def create_tarifa():
    data = request.get_json()
    tarifa = Tarifa(nombre=data['nombre'], descripcion=data['descripcion'])
    repo.adicionar(tarifa)
    return jsonify({"message": "Tarifa creada"}), 201

@app.route('/tarifas/<int:id>', methods=['GET'])
def read_tarifa(id):
    tarifa = repo.buscar(id)
    if tarifa:
        return jsonify({"id": tarifa.id, "nombre": tarifa.nombre, "descripcion": tarifa.descripcion}), 200
    return jsonify({"message": "Tarifa no encontrada"}), 404

@app.route('/tarifas/<int:id>', methods=['DELETE'])
def delete_tarifa(id):
    repo.eliminar(id)
    return jsonify({"message": "Tarifa eliminada"}), 204

@app.route('/tarifas/<int:id>', methods=['PUT'])
def update_tarifa(id):
    data = request.get_json()
    tarifa = repo.buscar(id)
    if tarifa:
        tarifa.nombre = data['nombre']
        tarifa.descripcion = data['descripcion']
        repo.actualizar(tarifa)
        return jsonify({"message": "Tarifa actualizada"}), 200
    return jsonify({"message": "Tarifa no encontrada"}), 404

api.add_namespace(ns)

