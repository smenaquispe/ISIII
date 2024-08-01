from ..interfaces.IGestionProyectos import IGestionProyectos
from ...domain.proyecto.factory import ProyectoFabrica
from ...repository.ProyectoRepositorio import ProyectoRepositorio

repositorio_proyecto=ProyectoRepositorio()
class GestionProyectos(IGestionProyectos):
    def crear_proyecto(self, data):
        nuevo_proyecto = ProyectoFabrica.crear_proyecto(
        id=data["id"],
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        estado=data['estado'],
        tipo=data['tipo'],
        presupuesto=data['presupuesto'],
        fecha_inicio=data['fecha_inicio'],
        fecha_fin=data['fecha_fin'],
        responsable=data['responsable']
        )
        respuesta, codigo= repositorio_proyecto.adicionar(nuevo_proyecto)
        return respuesta, codigo

    def actualizar_proyecto(self, data):
        nuevo_proyecto = ProyectoFabrica.crear_proyecto(
        id=data["id"],
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        estado=data['estado'],
        tipo=data['tipo'],
        presupuesto=data['presupuesto'],
        fecha_inicio=data['fecha_inicio'],
        fecha_fin=data['fecha_fin'],
        responsable=data['responsable']
        )
        respuesta, codigo = repositorio_proyecto.actualizar(nuevo_proyecto)
        return respuesta, codigo

    def buscar_proyecto(self, id):
        respuesta, codigo=repositorio_proyecto.buscar(id)
        return respuesta, codigo
    
    def eliminar_proyecto(self, id):
        respuesta, codigo=repositorio_proyecto.eliminar(id)
        return respuesta, codigo


