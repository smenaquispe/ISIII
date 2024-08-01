from flask import Flask
from gestion_integral_riesgos.api.controllers import init_app as riesgos_init_app


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('gestion_integral_riesgos/config_riesgos.py')

    with app.app_context():
        #from gestion_integral_riesgos.api.controllers import init_app as riesgos_init_app
        #from gestion_presupuestal.controllers import init_app as presupuestos_init_app
        #from gestion_proyectos.controllers import init_app as proyectos_init_app
        riesgos_init_app(app)
        #presupuestos_init_app(app)
        #proyectos_init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
