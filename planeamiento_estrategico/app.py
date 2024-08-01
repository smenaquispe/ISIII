from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Importar controladores para registrar las rutas
from controllers import *

if __name__ == '__main__':
    app.run(debug=True)
