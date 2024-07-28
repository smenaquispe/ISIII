from .models import Presupuesto

class PresupuestoFactory:
    @staticmethod
    def crear_presupuesto(nombre: str, descripcion: str, importe: float, aprobado: bool) -> Presupuesto:
        return Presupuesto(nombre=nombre, descripcion=descripcion, importe=importe, aprobado=aprobado)

    @staticmethod
    def solicitar_presupuesto(presupuesto: Presupuesto) -> None:
        pass

    @staticmethod
    def recopilar_presupuesto(presupuesto: Presupuesto) -> None:
        pass

    @staticmethod
    def revisar_presupuesto(presupuesto: Presupuesto) -> None:
        pass
