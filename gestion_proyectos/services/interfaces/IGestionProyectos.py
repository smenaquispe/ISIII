from abc import ABC,abstractmethod

class IGestionProyectos(ABC):
    @abstractmethod
    def crear_proyecto(self, data):
        pass
    @abstractmethod
    def eliminar_proyecto(self, id):
        pass
    @abstractmethod
    def actualizar_proyecto(self,data):
        pass
    @abstractmethod
    def buscar_proyecto(self, id):
        pass
