from datetime import date

class Proyecto:
    def __init__(self, id:int, nombre:str, descripcion:str, estado:str, tipo:str, presupuesto:float, fecha_inicio:str, fecha_fin:str, responsable:str):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.tipo = tipo
        self.presupuesto = presupuesto
        self.estudio = None
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.responsable = responsable

    