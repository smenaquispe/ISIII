from ..model.Estudio import Estudio
from datetime import date

def crear_estudio(id: int, nombre: str, descripcion: str, fecha_realizacion:str, costo:float, tipo:str, resultado:str) -> Estudio:
        nuevo_estudio= Estudio(id, nombre, descripcion, fecha_realizacion, costo, tipo, resultado)
        return nuevo_estudio