from flask import Blueprint, request, jsonify
from ...repository.EstudioRepositorio import EstudioRepositorio
from ...services.implementation.GestionEstudios import GestionEstudios
from flasgger import swag_from
#Subdominios creado /proyectos
proyectos_bp = Blueprint('estudio', __name__)

servicios_estudio=GestionEstudios()

#localhost:8080/proyectos/crear
@proyectos_bp.route('/crear', methods=['POST']) #solicitud que requiere de un servicio
def crear_estudio():
    """
    Crear un nuevo estudio
    ---
    tags:
      - Gestion de Estudio
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
              example: "Nuevo Estudio"
            descripcion:
              type: string
              example: "Descripción del estudio"
            fecha_realizacion:
              type: string
              format: date
              example: "2021-02-03"
            costo:
              type: number
              example: "10000"
            tipo:
              type: string
              example: "Preliminares"
            resultados:
              type: string
              example: "Aprobados"
    responses:
      201:
        description: Estudio creado
      400:
        description: No se pudo crear el estudio
    """
    data = request.json
    mensaje, codigo=servicios_estudio.crear_estudio(data)
    return jsonify(mensaje), codigo


#localhost:8080/estudio/buscar
@proyectos_bp.route('/buscar', methods=['GET'])
@swag_from({
    'tags': ['Gestion de Estudio'],
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
            'description': 'Detalles del estudio',
            'examples': {
                'application/json': {
                    'id': 1,
                    'nombre': 'Estudio de ejemplo',
                    'descripcion': 'Descripción de ejemplo',
                    'fecha_realizacion': '2024-01-01',
                    'costo': 100000,
                    'tipo': 'Preliminares',
                    'resultados': 'Aprobados'
                }
            }
        },
        404: {
            'description': 'Estudio no encontrado'
        }
    }
})
def buscar_estudio():
    # Obtener el id del parámetro de la URL
    estudio_id = request.args.get('id')
    resultado, codigo=servicios_estudio.buscar_estudio(estudio_id)
    return jsonify(resultado), codigo 

#localhost:8080/estudio/actualizar
@proyectos_bp.route("/actualizar", methods=["PUT"])
def actualizar_estudio():
    """
    Actualizar un nuevo estudio
    ---
    tags:
      - Gestion de Estudio
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
              example: "Nuevo Estudio"
            descripcion:
              type: string
              example: "Descripción del estudio"
            fecha_realizacion:
              type: string
              format: date
              example: "2021-02-03"
            costo:
              type: number
              example: "10000"
            tipo:
              type: string
              example: "Preliminares"
            resultados:
              type: string
              example: "Aprobados"
    responses:
      201:
        description: Estudio actualizado
      400:
        description: No se pudo actualizar el estudio
    """
    data = request.json
    mensaje, codigo=servicios_estudio.actualizar_estudio(data)
    return jsonify(mensaje), codigo

#localhost:8080/estudio/eliminar
@proyectos_bp.route("/eliminar", methods=["DELETE"])
@swag_from({
    'tags': ['Gestion de Estudio'],
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
            'description': 'Estudio eliminado exitosamente'
        },
        404: {
            'description': 'Estudio no encontrado'
        }
    }
})
def eliminar_estudio():
    estudio_id = request.args.get('id')
    mensaje, codigo=servicios_estudio.eliminar_estudio(estudio_id)
    return jsonify(mensaje), codigo

# Agrega las rutas al módulo de Flask
def init_app(app):
    app.register_blueprint(proyectos_bp, url_prefix='/estudio')