from uuid import uuid4
from app import db

class Tarifario:
    def __init__(self, nombre: str, descripcion: str, importe: float, aprobado: bool) -> None:
        self.id: str = str(uuid4())
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.importe: float = importe
        self.aprobado: bool = aprobado

class Tarifa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    importe = db.Column(db.Float, nullable=False)  # Si quieres añadir un campo para el importe


    def aprobar_tarifario(self) -> None:
        pass
