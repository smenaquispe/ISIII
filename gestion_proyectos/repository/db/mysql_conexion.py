import mysql.connector
from mysql.connector import Error

class BDMySql:
    def __init__(self) -> None:
        self._conexion=None
        self._user=None
        self._password=None
        self._database=None
        self._port=None

    def crear_conexion(self):
        try:
            self._conexion=mysql.connector.connect(
                user="root",
                password="27_KdB_Mc",
                host="localhost",
                database="sedapal",
                port="3306"
            )
            if(self._conexion.is_connected):
                print("Conexion exitosa")
        except Error as e:
            print("Error durante la conexion", e)


    def get_conexion(self):
        return self._conexion

    def cerrar_conexion(self)->None:
        self._conexion.close()
        print("Se cerro la conexion")


