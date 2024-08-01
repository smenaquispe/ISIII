from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Presupuesto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    importe = db.Column(db.Float, nullable=False)
    aprobado = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, nombre: str, descripcion: str, importe: float, aprobado: bool):
        self.nombre = nombre
        self.descripcion = descripcion
        self.importe = importe
        self.aprobado = aprobado
        
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'importe': self.importe,
            'aprobado': self.aprobado
        }
