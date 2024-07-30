from .models import Tarifario

class TarifarioFactory:
    @staticmethod
    def crear_tarifario(nombre: str, descripcion: str, importe: float, aprobado: bool) -> Tarifario:
        return Tarifario(nombre=nombre, descripcion=descripcion, importe=importe, aprobado=aprobado)

    @staticmethod
    def solicitar_tarifario(tarifario: Tarifario) -> None:
        pass

    @staticmethod
    def recopilar_tarifario(tarifario: Tarifario) -> None:
        pass

    @staticmethod
    def revisar_tarifario(tarifario: Tarifario) -> None:
        pass
