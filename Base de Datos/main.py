from Conexion import DatabaseConnection

print("****** SISTEMA DE REGISTRO DE PEDIDOS ******")

# Crear una instancia de DatabaseConnection
db_connection = DatabaseConnection(
    host="localhost",
    user="root",
    password="kali",
    port="3306",
    database="BigBread"
)
db_connection.connect()

num_pedidos = 0  # Variable para almacenar el número de pedidos

while True:
    opcion = input('Desea ingresar los datos requeridos para registrar su pedido? Presione "S" para continuar, "X" para salir: ').upper()

    if opcion == 'X':
        print('****** USTED HA SALIDO DEL SISTEMA DE REGISTRO DE PEDIDOS ******')
        break

    elif opcion == 'S':
        nombre = input('Ingrese el nombre del cliente: ')
        pedido = input(f'Ingrese el pedido de {nombre}: ')
        cantidad = input('Ingrese la cantidad: ')

        # Consultar la base de datos para obtener los precios de los productos del pedido
        cursor = db_connection.connection.cursor()
        query = "SELECT precio FROM Pedidos WHERE nombre = %s"
        cursor.execute(query, (pedido,))
        precios = cursor.fetchall()

        # Calcular el precio total sumando los precios de los productos y multiplicando por la cantidad
        precio_total = sum(precio[0] for precio in precios) * int(cantidad)

        # Insertar el pedido en la base de datos
        db_connection.insert_pedido(nombre, pedido, precio_total)
        num_pedidos += 1  # Incrementar el número de pedidos

        print("Pedido registrado exitosamente.")
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

# Mostrar el número de pedidos realizados hasta el momento
print("Número de pedidos realizados:", num_pedidos)

# Cerrar la conexión
db_connection.close()
