import mysql.connector
from conexion import *

# Definir la función insert_ingredientes
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



# Establecer la conexión a la base de datos
connection.connect()

# Insertar ingredientes
insert_ingredientes(connection, "mortadela")


# Insertar productos
insert_Productos(connection,1, "de mortadela ", 'mortadela y queso', '350')

# Crear un Select
cursor = connection.connection.cursor()
cursor.execute("SELECT * FROM productos;")
resultados = cursor.fetchall()

for row in resultados:
    print(row[0])

# Crear DELETE


cursor = connection.connection.cursor()
consulta = "DELETE FROM ingredientes WHERE nombre = %s"
valor = ("papas",)
cursor.execute(consulta, valor)
connection.connection.commit()



# Crear UPDATE
cursor = connection.connection.cursor()
consulta = "UPDATE productos SET Nombre = %s, Precio = %s  WHERE idProductos = %s"
valores = ("de anana", "500", 7)  # Reemplaza "7" con el valor correcto de idProductos
cursor.execute(consulta, valores)
connection.connection.commit()

cursor.close()

# Cerrar la conexión a la base de datos
connection.close()
