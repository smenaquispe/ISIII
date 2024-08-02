from flask import Blueprint, request, jsonify
from ...repository.ProyectoRepositorio import ProyectoRepositorio
from ...services.implementation.GestionProyectos import GestionProyectos
from flasgger import swag_from
#Subdominios creado /proyectos
proyectos_bp = Blueprint('proyecto', __name__)

servicios_proyecto=GestionProyectos()

#localhost:8080/proyectos/crear
@proyectos_bp.route('/crear', methods=['POST'])
#solicitud que requiere de un servicio
def crear_proyecto():
    """
    Crear un nuevo proyecto
    ---
    tags:
      - Gestion de Proyecto  
    parameters:
      - name: body
        in: body
        required: True
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            nombre:
              type: string
              example: "Nuevo Proyecto"
            descripcion:
              type: string
              example: "Descripción del proyecto"
            estado:
              type: string
              example: "activo"
            tipo:
              type: string
              example: "infraestructura"
            presupuesto:
              type: number
              example: 100000
            fecha_inicio:
              type: string
              format: date
              example: "2024-01-01"
            fecha_fin:
              type: string
              format: date
              example: "2024-12-31"
            responsable:
              type: string
              example: "Juan Pérez"
    responses:
      201:
        description: Proyecto creado
      400:
        description: No se pudo crear el proyecto
    """
    data = request.json
    mensaje, codigo=servicios_proyecto.crear_proyecto(data)
    return jsonify(mensaje), codigo


#localhost:8080/proyectos/buscar
@proyectos_bp.route('/buscar', methods=['GET'])
@swag_from({
    'tags': ['Gestion de Proyecto'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID del proyecto'
        }
    ],
    'responses': {
        200: {
            'description': 'Detalles del proyecto',
            'examples': {
                'application/json': {
                    'id': 1,
                    'nombre': 'Proyecto de ejemplo',
                    'descripcion': 'Descripción de ejemplo',
                    'estado': 'activo',
                    'tipo': 'infraestructura',
                    'presupuesto': 100000,
                    'fecha_inicio': '2024-01-01',
                    'fecha_fin': '2024-12-31',
                    'responsable': 'Juan Pérez'
                }
            }
        },
        404: {
            'description': 'Proyecto no encontrado'
        }
    }
})
def buscar_proyecto():

    # Obtener el id del parámetro de la URL
    proyecto_id = request.args.get('id')
    resultado, codigo=servicios_proyecto.buscar_proyecto(proyecto_id)
    return jsonify(resultado), codigo 

#localhost:8080/proyectos/actualizar
@proyectos_bp.route("/actualizar", methods=["PUT"])
def actualizar_proyecto():
    """
    Actualizar un nuevo proyecto
    ---
    tags:
      - Gestion de Proyecto  
    parameters:
      - name: body
        in: body
        required: True
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            nombre:
              type: string
              example: "Nuevo Proyecto"
            descripcion:
              type: string
              example: "Descripción del proyecto"
            estado:
              type: string
              example: "activo"
            tipo:
              type: string
              example: "infraestructura"
            presupuesto:
              type: number
              example: 100000
            fecha_inicio:
              type: string
              format: date
              example: "2024-01-01"
            fecha_fin:
              type: string
              format: date
              example: "2024-12-31"
            responsable:
              type: string
              example: "Juan Pérez"
    responses:
      200:
        description: Proyecto actualizado
      400:
        description: No se pudo actualizar el proyecto
    """
    data = request.json
    mensaje, codigo=servicios_proyecto.actualizar_proyecto(data)
    return jsonify(mensaje), codigo

#localhost:8080/proyectos/eliminar
@proyectos_bp.route("/eliminar", methods=["DELETE"])
@swag_from({
    'tags': ['Gestion de Proyecto'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID del proyecto'
        }
    ],
    'responses': {
        204: {
            'description': 'Proyecto eliminado exitosamente'
        },
        404: {
            'description': 'Proyecto no encontrado'
        }
    }
})
def eliminar_proyecto():
    proyecto_id = request.args.get('id')
    mensaje, codigo=servicios_proyecto.eliminar_proyecto(proyecto_id)
    return jsonify(mensaje), codigo

# Agrega las rutas al módulo de Flask
def init_app(app):
    app.register_blueprint(proyectos_bp, url_prefix='/proyecto')