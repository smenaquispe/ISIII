
from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from gestion_integral_riesgos.controllers import init_app as riesgos_init_app
        from gestion_presupuestal.controllers import init_app as presupuestos_init_app
        #controladores de proyecto y estudios
        from gestion_proyectos.presentacion.controllers.ProyectoController import init_app as proyectos_init_app
        #from gestion_proyectos.presentacion.controllers.EstudioController import init_app as estudios_init_app
        riesgos_init_app(app)
        presupuestos_init_app(app)
        proyectos_init_app(app)
        #estudios_init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
