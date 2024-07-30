from flask import Blueprint, request, jsonify
from .factory import EstrategiaFactory
from .repositories import EstrategiaRepository
from .services import EstrategiaService

estrategias_bp = Blueprint('estrategias', __name__)
estrategia_repo = EstrategiaRepository()
estragia_service = EstrategiaService()

@estrategias_bp.route('/crear', methods=['POST'])
def crear_riesgo():
    data = request.json
    nuevo_estrategia = EstrategiaFactory.crear_estrategia(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        importe=data['importe'],
        aprobado=data['aprobado']
    )
    estrategia_repo.adicionar(nuevo_estrategia)
    return jsonify({'message': 'Prespuesto creado'}), 201


@estrategias_bp.route('/informe', methods=['GET'])
def generar_informe():
    informe = estragia_service.corregir_estrategia()
    return jsonify({'informe': informe})

# Agrega las rutas al módulo de Flask
def init_app(app):
    app.register_blueprint(estrategias_bp, url_prefix='/estrategias')
