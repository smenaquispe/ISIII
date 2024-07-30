from flask import Blueprint, request, jsonify
from .factory import TarifarioFactory
from .repositories import TarifarioRepository
from .services import TarifarialService

tarifarios_bp = Blueprint('tarifarios', __name__)
tarifario_repo = TarifarioRepository()
tarifarial_service = TarifarialService()

@tarifarios_bp.route('/crear', methods=['POST'])
def crear_tarifario():
    data = request.json
    nuevo_tarifario = TarifarioFactory.crear_tarifario(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        importe=data['importe'],
        aprobado=data['aprobado']
    )
    tarifario_repo.adicionar(nuevo_tarifario)
    return jsonify({'message': 'Tarifa creado'}), 201


@tarifarios_bp.route('/informe', methods=['GET'])
def resolucion_informe():
    informe = tarifarial_service.resolucion_informe()
    return jsonify({'informe': informe})

# Agrega las rutas al módulo de Flask
def init_app(app):
    app.register_blueprint(tarifarios_bp, url_prefix='/tarifarios')
