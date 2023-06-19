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

def insert_Productos(connection, idProductos, Nombre, ingredientes, Precio):
    try:
        cursor = connection.connection.cursor()
        query = "INSERT INTO Productos (idProductos, Nombre, ingredientes, Precio) VALUES (%s, %s, %s, %s)"
        values = (idProductos, Nombre, ingredientes, Precio)
        cursor.execute(query, values)
        connection.connection.commit()
        print("Productos agregados exitosamente.")
    except mysql.connector.Error as err:
        print("Error al insertar Productos:", err)

# Crear una instancia de DatabaseConnection
db_connection = DatabaseConnection(
    host="localhost",
    user="root",
    password="Delfines/2",
    port=3306,
    database="Sandwiches_BigBread"
)

# Establecer la conexión a la base de datos
db_connection.connect()

# Insertar ingredientes con IDs específicos
insert_ingredientes(db_connection, 9, "roquefort")
insert_ingredientes(db_connection, 10, "nuez")
insert_ingredientes(db_connection, 11, "anana")
insert_ingredientes(db_connection, 12, "palmitos")
insert_ingredientes(db_connection, 13, "ternera")
insert_ingredientes(db_connection, 14, "huevo")

# Insertar productos con IDs específicos
insert_Productos(db_connection,  "de verdura", 'tomate, jamon, lechuga, queso', '350')
insert_Productos(db_connection,  "de roquefort", 'roquefort, nuez, jamon', '500')
insert_Productos(db_connection,  "de rucula", 'jamon crudo, rucula, queso', '350')
insert_Productos(db_connection,  "de anana", 'jamon, anana', '400')
insert_Productos(db_connection,  "de palmitos", 'jamon, palmitos', '400')
insert_Productos(db_connection,  "de ternera y verdura", 'ternera, tomate y huevo', '300')

# Crear un Select
cursor = db_connection.connection.cursor()
cursor.execute("SELECT * FROM productos;")
resultados = cursor.fetchall()

for row in resultados:
    print(row[0])

# Crear DELETE
cursor = db_connection.connection.cursor()
consulta = "DELETE FROM Pedidos WHERE columna = %s"
valor = ("rodilla",)

cursor.execute(consulta, valor)

# Crear UPDATE
cursor = db_connection.connection.cursor()
consulta = "UPDATE productos SET columna1 = %s, columna2 = %s WHERE condicion"
valores = ("de anana", "500")
cursor.execute(consulta, valores)
db_connection.connection.commit()

cursor.close()

# Cerrar la conexión a la base de datos
db_connection.close()

