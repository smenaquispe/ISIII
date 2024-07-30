from flask import Blueprint, request, jsonify
from .factory import PresupuestoFactory
from .repositories import PresupuestoRepository
from .services import PresupuestalService

presupuestos_bp = Blueprint('presupuestos', __name__)
presupuesto_repo = PresupuestoRepository()
presupuestal_service = PresupuestalService()

@presupuestos_bp.route('/crear', methods=['POST'])
def crear_riesgo():
    data = request.json
    nuevo_presupuesto = PresupuestoFactory.crear_presupuesto(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        importe=data['importe'],
        aprobado=data['aprobado']
    )
    presupuesto_repo.adicionar(nuevo_presupuesto)
    return jsonify({'message': 'Prespuesto creado'}), 201


@presupuestos_bp.route('/informe', methods=['GET'])
def generar_informe():
    informe = presupuestal_service.generar_informe()
    return jsonify({'informe': informe})

# Agrega las rutas al módulo de Flask
def init_app(app):
    app.register_blueprint(presupuestos_bp, url_prefix='/presupuestos')
