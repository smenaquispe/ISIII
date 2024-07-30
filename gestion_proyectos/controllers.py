from flask import Blueprint, request, jsonify
from .factory import ProyectoFactory
from .repositories import ProyectoRepository
from .services import LecitacionService
#Subdominios creado /proyectos
proyectos_bp = Blueprint('proyectos', __name__)

proyecto_repo = ProyectoRepository()
licitacion_service = LecitacionService()

#localhost:8080/proyectos/crear
@proyectos_bp.route('/crear', methods=['POST'])
def crear_riesgo():
    data = request.json
    nuevo_presupuesto = ProyectoFactory.crear_proyecto(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        estado=data['estado']
    )
    proyecto_repo.adicionar(nuevo_presupuesto)
    return jsonify({'message': 'Proyecto creado'}), 201

#localhost:8080/proyectos/verificar
@proyectos_bp.route('/verificar', methods=['GET'])
def generar_informe():
    verificacion = licitacion_service.verificar_presupuesto()
    return jsonify({'verificacion': verificacion})

# Agrega las rutas al módulo de Flask
def init_app(app):
    app.register_blueprint(proyectos_bp, url_prefix='/proyectos')
