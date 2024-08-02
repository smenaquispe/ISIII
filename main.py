from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
from swagger_config import swagger_config, swagger_ui_config
from gestion_integral_riesgos.api.riesgos.controllers import init_app as riesgos_init_app
from gestion_integral_riesgos.api.usuarios.controllers import init_app as usuarios_init_app

jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Configuración de Swagger
    SWAGGER_URL = '/swagger'
    API_URL = '/swagger.json'

    swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config=swagger_ui_config()
)

    app.config.from_pyfile('gestion_integral_riesgos/config_riesgos.py')
    app.config.from_pyfile('gestion_integral_riesgos/config_usuarios.py')

    @app.route("/swagger.json")
    def swagger_json():
        return jsonify(swagger_config())

    jwt.init_app(app)
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


    with app.app_context():
        #from gestion_integral_riesgos.api.controllers import init_app as riesgos_init_app
        #from gestion_presupuestal.controllers import init_app as presupuestos_init_app
        #from gestion_proyectos.controllers import init_app as proyectos_init_app
        riesgos_init_app(app)
        usuarios_init_app(app)
        #presupuestos_init_app(app)
        #proyectos_init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
