from .models import Presupuesto, db

class PresupuestoRepository:
    def adicionar(self, presupuesto: Presupuesto) -> None:
        db.session.add(presupuesto)
        db.session.commit()

    def eliminar(self, id: int) -> None:
        presupuesto = self.buscar(id)
        if presupuesto:
            db.session.delete(presupuesto)
            db.session.commit()

    def actualizar(self, presupuesto: Presupuesto) -> None:
        db.session.commit()

    def buscar(self, id: int) -> Presupuesto:
        return Presupuesto.query.get(id)

    def obtener_todos(self) -> list:
        return Presupuesto.query.all()
