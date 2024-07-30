from uuid import uuid4

class Presupuesto:
    def __init__(self, nombre: str, descripcion: str, importe: float, aprobado: bool) -> None:
        self.id: str = str(uuid4())
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.importe: float = importe
        self.aprobado: bool = aprobado

    def crear_presupuesto(self) -> None:
        pass

    def aprobar_presupuesto(self) -> None:
        pass
