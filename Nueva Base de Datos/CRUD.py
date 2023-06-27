import mysql.connector
from conexion import *
from entidades import *

#***********************************************************
# CRUD SELECT
# INGREDIENTES
class CRUD_Select:
    def select_ingredientes(connection):
        try:
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("SELECT Nombre FROM ingredientes;")
            resultados = cursor.fetchall()
            for row in resultados:
                print(row[1])  # Mostrar el nombre del ingrediente
        except mysql.connector.Error as err:
            print("Error al seleccionar ingredientes:", err)
# PRODUCTOS
    def select_productos(connection):
        try:
            connection.connect()
            cursor = connection.connection.cursor()
            query = "SELECT Nombre, Ingredientes, Precio FROM productos"
            cursor.execute(query)
            resultados = cursor.fetchall()

            print("======= LISTA DE PRODUCTOS =======")
            for row in resultados:
                print(f"Nombre: {row[0]}")
                print(f"Ingredientes: {row[1]}")
                print(f"Precio: {row[2]}")
                print("===============================")

        except mysql.connector.Error as err:
            print("Error al seleccionar productos:", err)

#***********************************************************
# CRUD AGREGAR
# INGREDIENTES
class CRUD_Insert:
    def insert_ingredientes(connection, nombre):
        try:
            connection.connect()
            cursor = connection.connection.cursor()
            query = "INSERT INTO ingredientes (Nombre) VALUES (%s)"
            values = (nombre,)
            cursor.execute(query, values)
            connection.connection.commit()
            print("Ingrediente agregado exitosamente.")
        except mysql.connector.Error as err:
            print("Error al insertar ingrediente:", err)
        finally:
            cursor.close()

# PRODUCTOS
    def insert_productos(connection, Nombre, ingredientes, Precio):
        try:
            connection.connect()
            cursor = connection.connection.cursor()
            query = "INSERT INTO productos (Nombre, Ingredientes, Precio) VALUES (%s, %s, %s)"
            values = (Nombre, ingredientes, Precio)
            cursor.execute(query, values)
            connection.connection.commit()
            print("Producto agregado exitosamente.")
        except mysql.connector.Error as err:
            print("Error al insertar Producto:", err)


#***********************************************************
# CRUD UPDATE
# INGREDIENTES
class CRUD_Update:
    def update_ingrediente(connection, Nombre, Precio, idIngredientes):
        try:
            connection.connect()
            cursor = connection.connection.cursor()
            consulta = "UPDATE ingredientes SET Nombre = %s, Precio = %s WHERE idIngredientes = %s"
            valores = (Nombre, Precio, idIngredientes)
            cursor.execute(consulta, valores)
            connection.connection.commit()
        except mysql.connector.Error as err:
            print("Error al actualizar ingrediente:", err)

    def update_producto(connection, Nombre, Precio, idProductos):
        try:
            connection.connect()
            cursor = connection.connection.cursor()
            consulta = "UPDATE productos SET Nombre = %s, Precio = %s WHERE idProductos = %s"
            valores = (Nombre, Precio, idProductos)
            cursor.execute(consulta, valores)
            connection.connection.commit()
        except mysql.connector.Error as err:
            print("Error al actualizar producto:", err)      

#***********************************************************
# CRUD DELETE
# INGREDIENTES
class CRUD_Delete:
    def delete_ingrediente(connection, nombre):
        try:
            connection.connect()
            cursor = connection.connection.cursor()
            consulta = "DELETE FROM ingredientes WHERE Nombre = %s"
            valor = (nombre,)
            cursor.execute(consulta, valor)
            connection.connection.commit()
        except mysql.connector.Error as err:
            print("Error al eliminar ingrediente:", err)

# PRODUCTOS
    def delete_productos(connection, nombre):
        try:
            connection.connect()
            cursor = connection.connection.cursor()
            consulta = "DELETE FROM productos WHERE Nombre = %s"
            valor = (nombre,)
            cursor.execute(consulta, valor)
            connection.connection.commit()
        except mysql.connector.Error as err:
            print("Error al eliminar ingrediente:", err)

#***********************************************************          

