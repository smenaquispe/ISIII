from .models import Presupuesto

class PresupuestoRepository:
    def __init__(self):
        self.presupuestos = {}

    def adicionar(self, presupuesto: Presupuesto) -> None:
        self.presupuestos[presupuesto.id] = presupuesto

    def eliminar(self, id) -> None:
        if id in self.presupuestos:
            del self.presupuestos[id]

    def actualizar(self, presupuesto: Presupuesto) -> None:
        self.presupuestos[presupuesto.id] = presupuesto

    def buscar(self, id) -> Presupuesto:
        return self.presupuestos.get(id)
