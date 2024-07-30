from flask import Blueprint, request, jsonify
from ...domain.proyecto import ProyectoFabrica
from ...domain.proyecto.IProyectoRepositorio import IProyectoRepositorio
#Subdominios creado /proyectos
proyectos_bp = Blueprint('proyecto', __name__)

interfaz_repositorio_proyecto=IProyectoRepositorio()

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
    interfaz_repositorio_proyecto.adicionar(nuevo_proyecto)
    return jsonify({'message': 'Proyecto creado'}), 201


#localhost:8080/proyectos/actualizar

#localhost:8080/proyectos/eliminar

#localhost:8080/proyectos/buscar

# Agrega las rutas al módulo de Flask
def init_app(app):
    app.register_blueprint(proyectos_bp, url_prefix='/proyecto')