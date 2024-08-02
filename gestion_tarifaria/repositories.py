from app import db
from models import Tarifa

class TarifaRepository:
    def adicionar(self, tarifa: Tarifa) -> None:
        db.session.add(tarifa)
        db.session.commit()

    def eliminar(self, id: int) -> None:
        tarifa = Tarifa.query.get(id)
        if tarifa:
            db.session.delete(tarifa)
            db.session.commit()

    def actualizar(self, tarifa: Tarifa) -> None:
        db.session.merge(tarifa)
        db.session.commit()

    def buscar(self, id: int) -> Tarifa:
        return Tarifa.query.get(id)
