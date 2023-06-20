import mysql.connector
from conexion import DatabaseConnection

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


# Crear una instancia de DatabaseConnection
db_connection = DatabaseConnection(
    host="localhost",
    user="root",
    password="**********",
    port=3306,
    database="Sandwiches_BigBread"
)

# Establecer la conexión a la base de datos
db_connection.connect()

# Insertar ingredientes
insert_ingredientes(db_connection, "mortadela")


# Insertar productos
insert_Productos(db_connection,1, "de mortadela ", 'mortadela y queso', '350')

# Crear un Select
cursor = db_connection.connection.cursor()
cursor.execute("SELECT * FROM productos;")
resultados = cursor.fetchall()

for row in resultados:
    print(row[0])

# Crear DELETE


cursor = db_connection.connection.cursor()
consulta = "DELETE FROM ingredientes WHERE nombre = %s"
valor = ("papas",)
cursor.execute(consulta, valor)
db_connection.connection.commit()



# Crear UPDATE
cursor = db_connection.connection.cursor()
consulta = "UPDATE productos SET Nombre = %s, Precio = %s  WHERE idProductos = %s"
valores = ("de anana", "500", 7)  # Reemplaza "7" con el valor correcto de idProductos
cursor.execute(consulta, valores)
db_connection.connection.commit()

cursor.close()

# Cerrar la conexión a la base de datos
db_connection.close()
