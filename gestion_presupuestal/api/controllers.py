from flask import Blueprint, request, jsonify
from .factory import PresupuestoFactory
from .repositories import PresupuestoRepository
from .services import PresupuestalService
from .models import db

presupuestos_bp = Blueprint('presupuestos', __name__)
presupuesto_repo = PresupuestoRepository()
presupuestal_service = PresupuestalService(presupuesto_repo)

@presupuestos_bp.route('/crear', methods=['POST'])
def crear_presupuesto():
    data = request.json
    nuevo_presupuesto = PresupuestoFactory.crear_presupuesto(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        importe=data['importe'],
        aprobado=data['aprobado']
    )
    presupuesto_repo.adicionar(nuevo_presupuesto)
    return jsonify({'message': 'Presupuesto creado', 'id': nuevo_presupuesto.id}), 201

@presupuestos_bp.route('/listar', methods=['GET'])
def listar_presupuestos():
    try:
        presupuestos = presupuesto_repo.obtener_todos()
        return jsonify([presupuesto.to_dict() for presupuesto in presupuestos]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@presupuestos_bp.route('/obtener/<int:id>', methods=['GET'])
def obtener_presupuesto(id):
    presupuesto = presupuesto_repo.buscar(id)
    if not presupuesto:
        return jsonify({'message': 'Presupuesto no encontrado'}), 404
    return jsonify({
        'id': presupuesto.id,
        'nombre': presupuesto.nombre,
        'descripcion': presupuesto.descripcion,
        'importe': presupuesto.importe,
        'aprobado': presupuesto.aprobado
    })

@presupuestos_bp.route('/actualizar/<id>', methods=['PUT'])
def actualizar_presupuesto(id):
    try:
        data = request.json
        presupuesto_existente = presupuesto_repo.buscar(id)
        if presupuesto_existente:
            presupuesto_existente.nombre = data['nombre']
            presupuesto_existente.descripcion = data['descripcion']
            presupuesto_existente.importe = data['importe']
            presupuesto_existente.aprobado = data['aprobado']
            presupuesto_repo.actualizar(presupuesto_existente)
            return jsonify({'message': 'Presupuesto actualizado exitosamente'}), 200
        else:
            return jsonify({'message': 'Presupuesto no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@presupuestos_bp.route('/eliminar/<id>', methods=['DELETE'])
def eliminar_presupuesto(id):
    try:
        if presupuesto_repo.buscar(id):
            presupuesto_repo.eliminar(id)
            return jsonify({'message': 'Presupuesto eliminado exitosamente'}), 200
        else:
            return jsonify({'message': 'Presupuesto no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@presupuestos_bp.route('/informe', methods=['GET'])
def generar_informe():
    informe = presupuestal_service.generar_informe()
    return jsonify({'informe': informe})



def init_app(app):
    app.config.from_pyfile('api/config.py')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(presupuestos_bp, url_prefix='/presupuestos')
