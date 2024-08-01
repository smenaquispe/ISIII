from app import app, db
from models import Estrategia

with app.app_context():
    db.create_all()
    print("Base de datos inicializada")
