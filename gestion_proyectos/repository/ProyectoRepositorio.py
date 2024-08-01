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
            
            agregar_proyecto = ("INSERT INTO proyecto (id, nombre, descripcion, "
                                "estado, tipo, presupuesto, fecha_inicio, fecha_fin, responsable) "
                                "VALUES (%(id)s, %(nombre)s, %(descripcion)s, %(estado)s, "
                                "%(tipo)s, %(presupuesto)s, %(fecha_inicio)s, %(fecha_fin)s, %(responsable)s)")
            
            cursor.execute(agregar_proyecto, diccionario)
            conexion.commit()
            
            return {"mensaje": "Proyecto creado"}, 201
        
        except mysql.connector.Error as err:
            # Manejo de errores específicos de MySQL
            print(f"Error: {err}")
            return {"mensaje": "Error al crear el proyecto"},404
        
        except Exception as e:
            # Manejo de errores generales
            print(f"Error: {e}")
            return {"mensaje": "Error inesperado"},404
        
        finally:
            if cursor:
                cursor.close()
            if conexion:
                bd.cerrar_conexion()


    def actualizar(self, proyecto):
        servicio_proyecto=ProyectoServicioDominio()
        diccionario=servicio_proyecto.obtener_diccionario(proyecto)
        bd = BDMySql()
        try:
            bd.crear_conexion()
            conexion = bd.get_conexion()
            cursor = conexion.cursor()
            
            query = ("UPDATE proyecto SET nombre=%(nombre)s,"
                                "descripcion=%(descripcion)s,estado=%(estado)s,"
                                "tipo=%(tipo)s, presupuesto=%(presupuesto)s,"
                                "fecha_inicio=%(fecha_inicio)s, fecha_fin=%(fecha_fin)s,"
                                "responsable=%(responsable)s WHERE id=%(id)s")
            
            cursor.execute(query, diccionario)
            conexion.commit()
            if cursor.rowcount == 0:
                return {"mensaje": "Proyecto no encontrado"}, 404
            return {"mensaje": "Proyecto actualizado correctamente"}, 200 
        
        except mysql.connector.Error as err:
            # Manejo de errores específicos de MySQL
            print(f"Error: {err}")
            return {"mensaje": "Error al actualizar el proyecto - MYSQL"},404
        
        except Exception as e:
            # Manejo de errores generales
            print(f"Error: {e}")
            return {"mensaje": "Error inesperado - GENERAL"},404
        
        finally:
            if cursor:
                cursor.close()
            if conexion:
                bd.cerrar_conexion()

    def eliminar(self, id):
        bd = BDMySql()
        try:
            bd.crear_conexion()
            conexion = bd.get_conexion()
            cursor = conexion.cursor()
            
            query = ("DELETE FROM proyecto WHERE id=%s")
            
            cursor.execute(query, (id,))
            conexion.commit()
            if cursor.rowcount == 0:
                return {"mensaje": "Proyecto no encontrado"}, 404
            return {"mensaje": "Proyecto eliminado correctamente"}, 200 
        
        except mysql.connector.Error as err:
            # Manejo de errores específicos de MySQL
            print(f"Error: {err}")
            return {"mensaje": "Error al eliminar el proyecto - MYSQL"},404
        
        except Exception as e:
            # Manejo de errores generales
            print(f"Error: {e}")
            return {"mensaje": "Error inesperado - GENERAL"},404
        
        finally:
            if cursor:
                cursor.close()
            if conexion:
                bd.cerrar_conexion()

    def buscar(self, id):
        bd = BDMySql()
        try:
            bd.crear_conexion()
            conexion = bd.get_conexion()
            cursor = conexion.cursor()
            
            query = ("SELECT * FROM proyecto WHERE id=%s")
            
            cursor.execute(query, (id,))
            resultado = cursor.fetchone()  # Obtener un solo resultado
        
            # Opcionalmente, podrías verificar si se encontró un resultado
            if resultado:
                diccionario = {
                    "id": resultado[0],
                    "nombre": resultado[1],
                    "descripcion": resultado[2],
                    "estado": resultado[3],
                    "tipo": resultado[4],
                    "presupuesto": resultado[5],
                    "fecha_inicio": resultado[6].strftime("%Y-%m-%d"),
                    "fecha_fin": resultado[7].strftime("%Y-%m-%d"),
                    "responsable": resultado[8]
                }
                return diccionario, 200
            return {"mensaje": "No hay ningun registro"}, 200
        
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
