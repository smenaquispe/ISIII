#!/usr/bin/python
#-*- coding: utf-8 -*-
from datetime import date

class Estudio:
    def __init__(self,id:int,nombre:str,descripcion:str, fecha_realizacion:date, costo: float, tipo:str, resultados:str )-> None:
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_realizacion = fecha_realizacion
        self.costo = costo
        self.tipo = tipo
        self.resultados = resultados
