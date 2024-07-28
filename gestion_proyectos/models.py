from uuid import uuid4

class Proyecto:
    def __init__(self, nombre: str, descripcion: str, estado: bool) -> None:
        self.id: str = str(uuid4())
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.estado: bool = estado

    def crear_proyecto(self) -> None:
        pass