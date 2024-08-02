def swagger_config():
   return {
      "swagger": "2.0",
      "info": {
         "title": "Gestion Integral de Riesgos API",
         "description": "API para gestionar riesgos",
         "version": "1.0.0"
      },
      "host": "localhost:5000",  # Cambia esto según tu configuración
      "basePath": "/",
      "schemes": [
         "http"
      ],
      "paths": {
         "/riesgos/crear": {
               "post": {
                  "summary": "Crear un nuevo riesgo",
                  "description": "Endpoint para crear un nuevo riesgo",
                  "parameters": [
                     {
                           "name": "body",
                           "in": "body",
                           "required": True,
                           "schema": {
                              "$ref": "#/definitions/Riesgo"
                           }
                     }
                  ],
                  "responses": {
                     "201": {
                           "description": "Riesgo creado"
                     },
                     "400": {
                           "description": "Error en la solicitud"
                     }
                  }
               }
         },
         "/riesgos/priorizar/{id}": {
               "put": {
                  "summary": "Priorizar un riesgo",
                  "description": "Endpoint para priorizar un riesgo existente",
                  "parameters": [
                     {
                           "name": "id",
                           "in": "path",
                           "required": True,
                           "type": "integer"
                     },
                     {
                           "name": "body",
                           "in": "body",
                           "required": True,
                           "schema": {
                              "$ref": "#/definitions/Prioridad"
                           }
                     }
                  ],
                  "responses": {
                     "200": {
                           "description": "Prioridad actualizada"
                     },
                     "404": {
                           "description": "Riesgo no encontrado"
                     }
                  }
               }
         },
         "/riesgos/eliminar/{id}": {
               "delete": {
                  "summary": "Eliminar un riesgo",
                  "description": "Endpoint para eliminar un riesgo existente",
                  "parameters": [
                     {
                           "name": "id",
                           "in": "path",
                           "required": True,
                           "type": "integer"
                     }
                  ],
                  "responses": {
                     "200": {
                           "description": "Riesgo eliminado"
                     },
                     "404": {
                           "description": "Riesgo no encontrado"
                     }
                  }
               }
         },
         "/riesgos/informe": {
               "get": {
                  "summary": "Generar informe",
                  "description": "Endpoint para generar un informe de riesgos",
                  "responses": {
                     "200": {
                           "description": "Informe generado"
                     }
                  }
               }
         }
      },
      "definitions": {
         "Riesgo": {
               "type": "object",
               "properties": {
                  "id": {
                     "type": "integer"
                  },
                  "nombre": {
                     "type": "string"
                  },
                  "descripcion": {
                     "type": "string"
                  },
                  "probabilidad": {
                     "type": "number",
                     "format": "float"
                  }
               }
         },
         "Prioridad": {
               "type": "object",
               "properties": {
                  "prioridad_alta": {
                     "type": "boolean"
                  }
               }
         }
      }
   }

def swagger_ui_config():
   return {
      "app_name": "Gestion Integral de Riesgos"
   }
