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
def generar_informe():
    # Obtener el id del parámetro de la URL
    proyecto_id = request.args.get('id')
    encontrado=interfaz_repositorio_proyecto.buscar(proyecto_id)
    if encontrado:
        return jsonify(encontrado)
    else:
        return jsonify({'error': 'Proyecto no encontrado'}), 404

#localhost:8080/proyectos/actualizar

#localhost:8080/proyectos/eliminar

# Agrega las rutas al módulo de Flask
def init_app(app):
    app.register_blueprint(proyectos_bp, url_prefix='/proyecto')