from abc import ABC,abstractmethod

class IEstudioRepositorio(ABC):
    @abstractmethod
    def adicionar(self, data):
        pass
    @abstractmethod
    def actualizar(self, data):
        pass
    @abstractmethod
    def eliminar(self, id):
        pass
    @abstractmethod
    def buscar(self, id):
        pass