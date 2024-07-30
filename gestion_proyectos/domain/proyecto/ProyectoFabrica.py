from .model.Proyecto import Proyecto
from datetime import date

def crear_proyecto(id: int, nombre: str, descripcion: str, estado:str, tipo:str, presupuesto:float, fecha_inicio:str,fecha_fin:str, responsable:str) -> Proyecto:
        nuevo_proyecto= Proyecto(id, nombre, descripcion, estado, tipo, presupuesto, fecha_inicio,fecha_fin, responsable)
        return nuevo_proyecto

