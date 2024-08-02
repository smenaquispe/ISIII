from ..interfaces.IGestionEstudios import IGestionEstudios
from ...domain.estudio.factory import EstudioFabrica
from ...repository.EstudioRepositorio import EstudioRepositorio

repositorio_estudio=EstudioRepositorio()
class GestionEstudios(IGestionEstudios):
    def crear_estudio(self, data):
        nuevo_estudio = EstudioFabrica.crear_estudio(
        id=data["id"],
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        fecha_realizacion=data['fecha_realizacion'],
        costo=data['costo'],
        tipo=data['tipo'],
        resultado=data['resultado'],
        )
        respuesta, codigo= repositorio_estudio.adicionar(nuevo_estudio)
        return respuesta, codigo

    def actualizar_estudio(self, data):
        nuevo_estudio = EstudioFabrica.crear_estudio(
        id=data["id"],
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        fecha_realizacion=data['fecha_realizacion'],
        costo=data['costo'],
        tipo=data['tipo'],
        resultado=data['resultado'],
        )
        respuesta, codigo = repositorio_estudio.actualizar(nuevo_estudio)
        return respuesta, codigo

    def buscar_estudio(self, id):
        respuesta, codigo=repositorio_estudio.buscar(id)
        return respuesta, codigo
    
    def eliminar_estudio(self, id):
        respuesta, codigo=repositorio_estudio.eliminar(id)
        return respuesta, codigo
