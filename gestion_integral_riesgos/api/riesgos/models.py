from .. import db

class Riesgo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    probabilidad = db.Column(db.Float, nullable=False)
    prioridad_alta = db.Column(db.Boolean, nullable=False,default=False)

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
