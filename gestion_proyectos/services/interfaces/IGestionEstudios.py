from abc import ABC,abstractmethod

class IGestionEstudios(ABC):
    @abstractmethod
    def crear_estudio(self, data):
        pass
    @abstractmethod
    def eliminar_estudio(self, id):
        pass
    @abstractmethod
    def actualizar_estudio(self,data):
        pass
    @abstractmethod
    def buscar_estudio(self, id):
        pass
