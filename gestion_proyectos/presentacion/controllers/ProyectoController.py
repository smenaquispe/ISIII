from flask import Blueprint, request, jsonify
from ...repository.ProyectoRepositorio import ProyectoRepositorio
from ...services.implementation.GestionProyectos import GestionProyectos
#Subdominios creado /proyectos
proyectos_bp = Blueprint('proyecto', __name__)

servicios_proyecto=GestionProyectos()

#localhost:8080/proyectos/crear
@proyectos_bp.route('/crear', methods=['POST']) #solicitud que requiere de un servicio
def crear_proyecto():
    data = request.json
    mensaje, codigo=servicios_proyecto.crear_proyecto(data)
    return jsonify(mensaje), codigo


#localhost:8080/proyectos/buscar
@proyectos_bp.route('/buscar', methods=['GET'])
def buscar_proyecto():
    # Obtener el id del parámetro de la URL
    proyecto_id = request.args.get('id')
    resultado, codigo=servicios_proyecto.buscar_proyecto(proyecto_id)
    return jsonify(resultado), codigo 

#localhost:8080/proyectos/actualizar
@proyectos_bp.route("/actualizar", methods=["PUT"])
def actualizar_proyecto():
    data = request.json
    mensaje, codigo=servicios_proyecto.actualizar_proyecto(data)
    return jsonify(mensaje), codigo

#localhost:8080/proyectos/eliminar
@proyectos_bp.route("/eliminar", methods=["DELETE"])
def eliminar_proyecto():
    proyecto_id = request.args.get('id')
    mensaje, codigo=servicios_proyecto.eliminar_proyecto(proyecto_id)
    return jsonify(mensaje), codigo

# Agrega las rutas al módulo de Flask
def init_app(app):
    app.register_blueprint(proyectos_bp, url_prefix='/proyecto')