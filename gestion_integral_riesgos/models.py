from flask_sqlalchemy import SQLAlchemy

db_riesgos = SQLAlchemy()

class Riesgo(db_riesgos.Model):

    id = db_riesgos.Column(db_riesgos.Integer, primary_key=True)
    nombre = db_riesgos.Column(db_riesgos.String(80), nullable=False)
    descripcion = db_riesgos.Column(db_riesgos.String(200), nullable=False)
    probabilidad = db_riesgos.Column(db_riesgos.Float, nullable=False)
    prioridad_alta = db_riesgos.Column(db_riesgos.Boolean, nullable=False,default=False)

    def __init__(self,id: int, nombre: str, descripcion: str, probabilidad: float):
        self.id: int = id
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.probabilidad: float = probabilidad
        self.prioridad_alta: bool = False

    def crear_riesgo(self) -> None:
        pass

    def priorizar_riesgo(self) -> None:
        pass
