from .models import Riesgo, db_riesgos

class RiesgosRepository:

    def adicionar(self, riesgo: Riesgo) -> None:
        db_riesgos.session.add(riesgo)
        db_riesgos.session.commit()

    def eliminar(self, id:str) -> None:
        riesgo = self.buscar(id)
        if riesgo:
            db_riesgos.session.delete(riesgo)
            db_riesgos.session.commit()

    def actualizar(self, riesgo: Riesgo) -> None:
        db_riesgos.session.commit()

    def buscar(self, id) -> Riesgo:
        return db_riesgos.session.query(Riesgo).filter_by(id=id).first()

    def obtener_todos(self) -> list:
        return Riesgo.query.all()
