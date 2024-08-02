from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='Estrategias API',
          description='A simple API for managing estrategias', doc='/swagger')

ns = api.namespace('estrategias', description='Operations related to estrategias')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Importar controladores para registrar las rutas
from controllers import *

if __name__ == '__main__':
    app.run(debug=True)
