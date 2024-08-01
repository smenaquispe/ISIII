class PresupuestalService:
    def __init__(self, presupuesto_repo):
        self.presupuesto_repo = presupuesto_repo

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
