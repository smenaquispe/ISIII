from abc import ABC,abstractmethod

class IProyectoRepositorio(ABC):
    @abstractmethod
    def adicionar(self, proyecto):
        pass
    @abstractmethod
    def actualizar(self, proyecto, id):
        pass
    @abstractmethod
    def eliminar(self, id):
        pass
    @abstractmethod
    def buscar(self, id):
        pass

        
