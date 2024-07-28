from flask import Blueprint, request, jsonify
from .factory import RiesgoFactory
from .repositories import RiesgosRepository
from .services import MonitoreoService

riesgos_bp = Blueprint('riesgos', __name__)
riesgo_repo = RiesgosRepository()
monitoreo_service = MonitoreoService()

@riesgos_bp.route('/crear', methods=['POST'])
def crear_riesgo() -> tuple:
    data = request.json
    nuevo_riesgo = RiesgoFactory.crear_riesgo(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        probabilidad=data['probabilidad']
    )
    riesgo_repo.adicionar(nuevo_riesgo)
    return jsonify({'message': 'Riesgo creado'}), 201

@riesgos_bp.route('/informe', methods=['GET'])
def generar_informe() -> tuple:
    informe = monitoreo_service.generar_informe()
    return jsonify({'informe': informe})

def init_app(app) -> None:
    app.register_blueprint(riesgos_bp, url_prefix='/riesgos')
