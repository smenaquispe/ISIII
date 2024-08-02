from .models import Tarifa

class TarifaFactory:
    @staticmethod
    def crear_tarifa(nombre: str, descripcion: str, aprobado: bool) -> Tarifa:
        return Tarifa(nombre=nombre, descripcion=descripcion, aprobado=aprobado)

    @staticmethod
    def evaluar_tarifa(tarifa: Tarifa) -> None:
        pass
