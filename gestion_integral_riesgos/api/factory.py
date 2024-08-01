from gestion_integral_riesgos.api.models import Riesgo

class RiesgoFactory:
    @staticmethod
    def crear_riesgo(id:int,nombre: str, descripcion: str, probabilidad: float) -> Riesgo:
        return Riesgo(id=id,nombre=nombre, descripcion=descripcion, probabilidad=probabilidad)

    @staticmethod
    def priorizar_riesgo(riesgo) -> None:
        pass
