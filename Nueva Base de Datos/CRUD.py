import mysql.connector
from conexion import *
from entidades import *

class CRUD:
    @staticmethod
    def insert_ingredientes(connection, nombre):
        try:
            cursor = connection.connection.cursor()
            query = "INSERT INTO Ingredientes (nombre) VALUES (%s)"
            values = (nombre,)
            cursor.execute(query, values)
            connection.connection.commit()
            print("Ingrediente agregado exitosamente.")
        except mysql.connector.Error as err:
            print("Error al insertar ingrediente:", err)

    @staticmethod
    def insert_Productos(connection, Nombre, ingredientes, Precio):
        try:
            cursor = connection.connection.cursor()
            query = "INSERT INTO Productos (Nombre, ingredientes, Precio) VALUES (%s, %s, %s)"
            values = (Nombre, ingredientes, Precio)
            cursor.execute(query, values)
            connection.connection.commit()
            print("Producto agregado exitosamente.")
        except mysql.connector.Error as err:
            print("Error al insertar Producto:", err)