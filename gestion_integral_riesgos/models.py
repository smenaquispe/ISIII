from uuid import uuid4

class Riesgo:
    def __init__(self, nombre: str, descripcion: str, probabilidad: float):
        self.id: str = str(uuid4())
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.probabilidad: float = probabilidad

    def crear_riesgo(self) -> None:
        pass

    def priorizar_riesgo(self) -> None:
        pass
