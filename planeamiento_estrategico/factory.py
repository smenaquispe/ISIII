from .models import Estrategia

class EstrategiaFactory:
    @staticmethod
    def crear_estrategia(nombre: str, descripcion: str, aprobado: bool) -> Estrategia:
        return Estrategia(nombre=nombre, descripcion=descripcion, aprobado=aprobado)

    @staticmethod
    def evaluar_estrategia(estrategia: Estrategia) -> None:
        pass
