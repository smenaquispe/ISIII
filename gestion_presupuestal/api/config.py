import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_DIR = os.path.join(BASE_DIR, "database")

# Crear el directorio de la base de datos si no existe
if not os.path.exists(DATABASE_DIR):
    os.makedirs(DATABASE_DIR)

SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(DATABASE_DIR, "presupuestos.db")}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
