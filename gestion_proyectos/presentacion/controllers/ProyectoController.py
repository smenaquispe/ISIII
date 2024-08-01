from flask import Blueprint, request, jsonify
from ...domain.proyecto.factory import ProyectoFabrica
from ...repository.ProyectoRepositorio import ProyectoRepositorio
#Subdominios creado /proyectos
proyectos_bp = Blueprint('proyecto', __name__)

repositorio_proyecto=ProyectoRepositorio()

#localhost:8080/proyectos/crear
@proyectos_bp.route('/crear', methods=['POST']) #solicitud que requiere de un servicio
def crear_proyecto():
    data = request.json
    nuevo_proyecto = ProyectoFabrica.crear_proyecto(
        id=data["id"],
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        estado=data['estado'],
        tipo=data['tipo'],
        presupuesto=data['presupuesto'],
        fecha_inicio=data['fecha_inicio'],
        fecha_fin=data['fecha_fin'],
        responsable=data['responsable']
    )
    mensaje, codigo=repositorio_proyecto.adicionar(nuevo_proyecto)
    return jsonify(mensaje), codigo


#localhost:8080/proyectos/buscar
@proyectos_bp.route('/buscar', methods=['GET'])
def buscar_proyecto():
    # Obtener el id del parámetro de la URL
    proyecto_id = request.args.get('id')
    resultado, codigo=repositorio_proyecto.buscar(proyecto_id)
    return jsonify(resultado), codigo 

#localhost:8080/proyectos/actualizar
@proyectos_bp.route("/actualizar", methods=["PUT"])
def actualizar_proyecto():
    data = request.json
    nuevo_proyecto = ProyectoFabrica.crear_proyecto(
        id=data["id"],
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        estado=data['estado'],
        tipo=data['tipo'],
        presupuesto=data['presupuesto'],
        fecha_inicio=data['fecha_inicio'],
        fecha_fin=data['fecha_fin'],
        responsable=data['responsable']
    )
    mensaje, codigo=repositorio_proyecto.actualizar(nuevo_proyecto)
    return jsonify(mensaje), codigo



#localhost:8080/proyectos/eliminar

# Agrega las rutas al módulo de Flask
def init_app(app):
    app.register_blueprint(proyectos_bp, url_prefix='/proyecto')