from app import db
from models import Estrategia

class EstrategiaRepository:
    def adicionar(self, estrategia: Estrategia) -> None:
        db.session.add(estrategia)
        db.session.commit()

    def eliminar(self, id: int) -> None:
        estrategia = Estrategia.query.get(id)
        if estrategia:
            db.session.delete(estrategia)
            db.session.commit()

    def actualizar(self, estrategia: Estrategia) -> None:
        db.session.merge(estrategia)
        db.session.commit()

    def buscar(self, id: int) -> Estrategia:
        return Estrategia.query.get(id)
