from ..domain.estudio.repository.IEstudioRepositorio import IEstudioRepositorio
#from ..domain.estudio.services.EstudioServiciosDominio import ProyectoServicioDominio
from ..repository.db.mysql_conexion import BDMySql
import mysql.connector

class EstudioRepositorio(IEstudioRepositorio):
    def adicionar(self, estudio):
        diccionario=vars(estudio)
        bd = BDMySql()
        try:
            bd.crear_conexion()
            conexion = bd.get_conexion()
            cursor = conexion.cursor()
            
            query = ("INSERT INTO estudio (id, nombre, descripcion,fecha_realizacion, costo, tipo, resultado) "
                    "VALUES (%(id)s, %(nombre)s, %(descripcion)s, %(fecha_realizacion)s, "
                    "%(costo)s, %(tipo)s, %(resultado)s)")
            
            cursor.execute(query, diccionario)
            conexion.commit()
            
            return {"mensaje": "Estudio creado"}, 201
        
        except mysql.connector.Error as err:
            # Manejo de errores específicos de MySQL
            print(f"Error: {err}")
            return {"mensaje": "Error al crear el estudio"},404
        
        except Exception as e:
            # Manejo de errores generales
            print(f"Error: {e}")
            return {"mensaje": "Error inesperado"},404
        
        finally:
            if cursor:
                cursor.close()
            if conexion:
                bd.cerrar_conexion()


    def actualizar(self, estudio):
        diccionario=vars(estudio)
        bd = BDMySql()
        try:
            bd.crear_conexion()
            conexion = bd.get_conexion()
            cursor = conexion.cursor()
            
            query = ("UPDATE estudio SET nombre=%(nombre)s,"
                                "descripcion=%(descripcion)s,fecha_realizacion=%(fecha_realizacion)s,"
                                "costo=%(costo)s, tipo=%(tipo)s,"
                                "resultado=%(resultado)s WHERE id=%(id)s")
            
            cursor.execute(query, diccionario)
            conexion.commit()
            if cursor.rowcount == 0:
                return {"mensaje": "Estudio no encontrado"}, 404
            return {"mensaje": "Estudio actualizado correctamente"}, 200 
        
        except mysql.connector.Error as err:
            # Manejo de errores específicos de MySQL
            print(f"Error: {err}")
            return {"mensaje": "Error al actualizar el estudio - MYSQL"},404
        
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
            
            query = ("DELETE FROM estudio WHERE id=%s")
            
            cursor.execute(query, (id,))
            conexion.commit()
            if cursor.rowcount == 0:
                return {"mensaje": "Estudio no encontrado"}, 404
            return {"mensaje": "Estudio eliminado correctamente"}, 200 
        
        except mysql.connector.Error as err:
            # Manejo de errores específicos de MySQL
            print(f"Error: {err}")
            return {"mensaje": "Error al eliminar el estudio - MYSQL"},404
        
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
            
            query = ("SELECT * FROM estudio WHERE id=%s")
            
            cursor.execute(query, (id,))
            resultado = cursor.fetchone()  # Obtener un solo resultado
        
            # Opcionalmente, podrías verificar si se encontró un resultado
            if resultado:
                diccionario = {
                    "id": resultado[0],
                    "nombre": resultado[1],
                    "descripcion": resultado[2],
                    "fecha_realizacion": resultado[3].strftime("%Y-%m-%d"),
                    "costo": resultado[4],
                    "tipo": resultado[5],
                    "resultado": resultado[6]
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
