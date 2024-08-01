from ..domain.proyecto.repository.IProyectoRepositorio import IProyectoRepositorio
from ..domain.proyecto.services.ProyectoServiciosDominio import ProyectoServicioDominio
from ..repository.db.mysql_conexion import BDMySql
import mysql.connector

class ProyectoRepositorio(IProyectoRepositorio):
    def adicionar(self, proyecto):
        servicio_proyecto=ProyectoServicioDominio()
        diccionario=servicio_proyecto.obtener_diccionario(proyecto)
        bd = BDMySql()
        try:
            bd.crear_conexion()
            conexion = bd.get_conexion()
            cursor = conexion.cursor()
            
            agregar_proyecto = ("INSERT INTO Proyecto (id, nombre, descripcion, "
                                "estado, tipo, presupuesto, fecha_inicio, fecha_fin, responsable) "
                                "VALUES (%(id)s, %(nombre)s, %(descripcion)s, %(estado)s, "
                                "%(tipo)s, %(presupuesto)s, %(fecha_inicio)s, %(fecha_fin)s, %(responsable)s)")
            
            cursor.execute(agregar_proyecto, diccionario)
            conexion.commit()
            
            return {"mensaje": "Proyecto creado"}, 201
        
        except mysql.connector.Error as err:
            # Manejo de errores específicos de MySQL
            print(f"Error: {err}")
            return {"mensaje": "Error al crear el proyecto"}
        
        except Exception as e:
            # Manejo de errores generales
            print(f"Error: {e}")
            return {"mensaje": "Error inesperado"}
        
        finally:
            if cursor:
                cursor.close()
            if conexion:
                bd.cerrar_conexion()


    def actualizar(self, proyecto):
        pass

    def eliminar(self, proyecto):
        pass

    def buscar(self, id):
        pass
