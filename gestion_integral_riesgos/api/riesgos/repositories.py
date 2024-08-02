from gestion_integral_riesgos.api.riesgos.models import Riesgo
from .. import db

class RiesgosRepository:

    def adicionar(self, riesgo: Riesgo) -> None:
        db.session.add(riesgo)
        db.session.commit()

    def eliminar(self, id:str) -> None:
        riesgo = self.buscar(id)
        if riesgo:
            db.session.delete(riesgo)
            db.session.commit()

    def actualizar(self, riesgo: Riesgo) -> None:
        db.session.commit()

    def buscar(self, id) -> Riesgo:
        return db.session.query(Riesgo).filter_by(id=id).first()

    def obtener_todos(self) -> list:
        return Riesgo.query.all()
