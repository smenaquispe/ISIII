from flask import Blueprint, request, jsonify
from ...repository.EstudioRepositorio import EstudioRepositorio
from ...services.implementation.GestionEstudios import GestionEstudios
#Subdominios creado /proyectos
proyectos_bp = Blueprint('estudio', __name__)

servicios_estudio=GestionEstudios()

#localhost:8080/proyectos/crear
@proyectos_bp.route('/crear', methods=['POST']) #solicitud que requiere de un servicio
def crear_estudio():
    data = request.json
    mensaje, codigo=servicios_estudio.crear_estudio(data)
    return jsonify(mensaje), codigo


#localhost:8080/estudio/buscar
@proyectos_bp.route('/buscar', methods=['GET'])
def buscar_estudio():
    # Obtener el id del parámetro de la URL
    estudio_id = request.args.get('id')
    resultado, codigo=servicios_estudio.buscar_estudio(estudio_id)
    return jsonify(resultado), codigo 

#localhost:8080/estudio/actualizar
@proyectos_bp.route("/actualizar", methods=["PUT"])
def actualizar_estudio():
    data = request.json
    mensaje, codigo=servicios_estudio.actualizar_estudio(data)
    return jsonify(mensaje), codigo

#localhost:8080/estudio/eliminar
@proyectos_bp.route("/eliminar", methods=["DELETE"])
def eliminar_estudio():
    estudio_id = request.args.get('id')
    mensaje, codigo=servicios_estudio.eliminar_estudio(estudio_id)
    return jsonify(mensaje), codigo

# Agrega las rutas al módulo de Flask
def init_app(app):
    app.register_blueprint(proyectos_bp, url_prefix='/estudio')