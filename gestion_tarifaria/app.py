from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='Tarifas API',
          description='A simple API for managing tarifas', doc='/swagger')

ns = api.namespace('tarifas', description='Operations related to tarifas')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Importar controladores para registrar las rutas
from controllers import *

if __name__ == '__main__':
    app.run(debug=True)

