from .models import Riesgo

class RiesgoFactory:
    @staticmethod
    def crear_riesgo(nombre: str, descripcion: str, probabilidad: float) -> Riesgo:
        return Riesgo(nombre=nombre, descripcion=descripcion, probabilidad=probabilidad)

    @staticmethod
    def priorizar_riesgo(riesgo) -> None:
        pass
