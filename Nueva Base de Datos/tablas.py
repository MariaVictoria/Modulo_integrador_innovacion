import mysql.connector
from conexion import DatabaseConnection

# Definir la función insert_ingredientes
def insert_ingredientes(connection, id_ingredientes, nombre):
    try:
        cursor = connection.connection.cursor()
        query = "INSERT INTO Ingredientes (idIngredientes, nombre) VALUES (%s, %s)"
        values = (id_ingredientes, nombre)
        cursor.execute(query, values)
        connection.connection.commit()
        print("Ingrediente agregado exitosamente.")
    except mysql.connector.Error as err:
        print("Error al insertar ingrediente:", err)

def insert_Productos(connection, idProductos,Nombre, ingredientes,Precio ):
    try:
        cursor = connection.connection.cursor()
        query = "INSERT INTO Productos (idProductos,Nombre, ingredientes,Precio) VALUES (%s, %s, %s, %s)"
        values = (idProductos,Nombre, ingredientes,Precio)
        cursor.execute(query, values)
        connection.connection.commit()
        print("Productos agregado exitosamente.")
    except mysql.connector.Error as err:
        print("Error al insertar Productos:", err)
# Crear una instancia de DatabaseConnection
db_connection = DatabaseConnection(
    host="localhost",
    user="root",
    password="kali",
    port=3306,
    database="Sandwiches_BigBread"
)

# Establecer la conexión a la base de datos
db_connection.connect()

# Insertar ingredientes con IDs específicos
insert_ingredientes(db_connection, 8, "rucula")

# Insertar productos con IDs específicos
insert_Productos(db_connection, 2, "queso", 'queso','250')


# Cerrar la conexión a la base de datos
db_connection.close()
