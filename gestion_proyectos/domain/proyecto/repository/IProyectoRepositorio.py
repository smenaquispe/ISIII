from abc import ABC,abstractmethod

class IProyectoRepositorio(ABC):
    @abstractmethod
    def adicionar(self, proyecto):
        pass
    @abstractmethod
    def actualizar(self, proyecto):
        pass
    @abstractmethod
    def eliminar(self, proyecto):
        pass
    @abstractmethod
    def buscar(self, id):
        pass
    """
        # Buscar el proyecto por id
        proyecto = next((p for p in proyectos if p["id"] == id), None)
        return proyecto"""
        
