from uuid import uuid4

class Estrategia:
    def __init__(self, nombre: str, descripcion: str, aprobado: bool) -> None:
        self.id: str = str(uuid4())
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.aprobado: bool = aprobado

    def crear_estrategia(self) -> None:
        pass

    def evaluar_estrategia(self) -> None:
        pass
