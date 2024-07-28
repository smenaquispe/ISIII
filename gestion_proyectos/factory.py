from .models import Proyecto

class ProyectoFactory:
    @staticmethod
    def crear_proyecto(nombre: str, descripcion: str, estado: bool) -> Proyecto:
        return Proyecto(nombre=nombre, descripcion=descripcion, estado=estado)

    @staticmethod
    def solicitar_proyecto(proyecto: Proyecto) -> None:
        pass

    @staticmethod
    def recopilar_proyecto(proyecto: Proyecto) -> None:
        pass

    @staticmethod
    def revisar_proyecto(proyecto: Proyecto) -> None:
        pass
