from flask import Blueprint, request, jsonify
from .factory import RiesgoFactory
from .repositories import RiesgosRepository
from .services import MonitoreoService
from .models import db_riesgos

riesgos_bp = Blueprint('riesgos', __name__)
riesgo_repo = RiesgosRepository()
monitoreo_service = MonitoreoService(riesgo_repo)

@riesgos_bp.route('/crear', methods=['POST'])
def crear_riesgo() -> tuple:
    data = request.json
    nuevo_riesgo = RiesgoFactory.crear_riesgo(
        id = data['id'],
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        probabilidad=data['probabilidad']
    )
    riesgo_repo.adicionar(nuevo_riesgo)
    return jsonify({'message': 'Riesgo creado','id': nuevo_riesgo.id}), 201

@riesgos_bp.route('/informe', methods=['GET'])
def generar_informe() -> tuple:
    informe = monitoreo_service.generar_informe()
    return jsonify({'informe': informe})

def init_app(app) -> None:
    app.config.from_pyfile('config_riesgos.py')
    db_riesgos.init_app(app)
    with app.app_context():
        db_riesgos.create_all()
    app.register_blueprint(riesgos_bp, url_prefix='/riesgos')
