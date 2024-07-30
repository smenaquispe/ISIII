from .repositories import PresupuestoRepository

class PresupuestalService:
    def __init__(self):
        self.informe_presupuesto: str = ""
        self.presupuesto_repo = PresupuestoRepository()
    
    def verificar_presupuesto(self) -> None:
        pass

    def generar_informe(self) -> list:
        presupuestos = self.presupuesto_repo.obtener_todos()
        informe = []
        for idx, presupuesto in enumerate(presupuestos, 1):
            presupuesto_info = {
                'indice': idx,
                'id': presupuesto.id,
                'nombre': presupuesto.nombre,
                'descripcion': presupuesto.descripcion,
                'importe': presupuesto.importe,
                'aprobado': presupuesto.aprobado
            }
            informe.append(presupuesto_info)
        return informe
