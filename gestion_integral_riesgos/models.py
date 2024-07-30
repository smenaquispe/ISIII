from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy

db_riesgos = SQLAlchemy()

class Riesgo(db_riesgos.Model):

    id = db_riesgos.Column(db_riesgos.String, primary_key=True)
    nombre = db_riesgos.Column(db_riesgos.String(80), nullable=False)
    descripcion = db_riesgos.Column(db_riesgos.String(200), nullable=False)
    probabilidad = db_riesgos.Column(db_riesgos.Float, nullable=False)

    def __init__(self, nombre: str, descripcion: str, probabilidad: float):
        self.id: str = str(uuid4())
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.probabilidad: float = probabilidad

    def crear_riesgo(self) -> None:
        pass

    def priorizar_riesgo(self) -> None:
        pass
