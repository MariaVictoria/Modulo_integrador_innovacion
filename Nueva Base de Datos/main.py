import mysql.connector
from conexion import DatabaseConnection

def insert_pedidos(connection, cliente, Productos, precio, idProductos):
    try:
        cursor = connection.connection.cursor()
        query = "INSERT INTO Pedidos (cliente, Productos, Precio, idProductos) VALUES (%s, %s, %s, %s)"
        values = (cliente, Productos, precio, idProductos)
        cursor.execute(query, values)
        connection.connection.commit()
        print("Pedido agregado exitosamente.")
    except mysql.connector.Error as err:
        print("Error al insertar pedido:", err)

print("****** SISTEMA DE REGISTRO DE PEDIDOS ******")

# Crear una instancia de DatabaseConnection
db_connection = DatabaseConnection(
    host="localhost",
    user="root",
    password="******",
    port="3306",
    database="Sandwiches_BigBread"
)
db_connection.connect()

num_pedidos = 0  # Variable para almacenar el número de pedidos

while True:
    opcion = input('Desea ingresar los datos requeridos para registrar su pedido? Presione "S" para continuar, "X" para salir: ').upper()

    if opcion == 'X':
        print('****** USTED HA SALIDO DEL SISTEMA DE REGISTRO DE PEDIDOS ******')
        break

    elif opcion == 'S':
        cliente = input('Ingrese el nombre del cliente: ')
        pedido_completo = False
        total_pedido = 0

        while not pedido_completo:
            Productos = input(f'Ingrese el pedido de {cliente}: ')
            cantidad = int(input('Ingrese la cantidad: '))
            # Consultar la base de datos para obtener los precios de los productos del pedido
            cursor = db_connection.connection.cursor()
            query = "SELECT Precio, idProductos FROM Productos WHERE Nombre = %s"
            cursor.execute(query, (Productos,))
            productos = cursor.fetchall()

            # Verificar si se encontró el producto
            if len(productos) == 0:
                print("El producto ingresado no existe.")
                continue

            precio_producto, id_producto = productos[0]

            # Calcular el precio parcial del producto multiplicando el precio por la cantidad
            precio_parcial = precio_producto * cantidad

            total_pedido += precio_parcial

            # Insertar el pedido en la base de datos
            insert_pedidos(db_connection, cliente, Productos, precio_parcial, id_producto)
            num_pedidos += 1  # Incrementar el número de pedidos

            respuesta = input("¿Desea agregar otro producto? (Sí/No): ").lower()
            if respuesta == "no":
                pedido_completo = True

        print(f"Pedido registrado exitosamente. El monto a abonar es de: ${total_pedido}")

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

# Mostrar el número de pedidos realizados hasta el momento
print("Número de pedidos realizados:", num_pedidos)

