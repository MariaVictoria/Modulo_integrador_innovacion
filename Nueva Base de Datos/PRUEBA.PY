import mysql.connector

# Conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Delfines/2",
    database="Sandwiches_BigBread"
)

 #Función para ingresar un pedido
def ingresar_pedido():
    cliente = input("Ingrese el nombre del cliente: ")
    pedido = input("Ingrese el pedido: ")
    cantidad = int(input("Ingrese la cantidad: "))

    # Consultar el precio del producto
    cursor = conexion.cursor()
    cursor.execute("SELECT precio FROM productos WHERE nombre = %s", (pedido,))
    precio = cursor.fetchone()

    if precio:
        precio_total = precio[0] * cantidad
        print(f"Precio total a pagar: {precio_total}")
        # Guardar el pedido en la base de datos
        cursor.execute("INSERT INTO pedidos (cliente, pedido, cantidad, precio_total) VALUES (%s, %s, %s, %s)",
                       (cliente, pedido, cantidad, precio_total))
        conexion.commit()
        print("Pedido guardado exitosamente.")
    else:
        print("El producto no existe.")

    cursor.close()

# Función para consultar los productos disponibles
def consultar_productos():
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre FROM productos")
    productos = cursor.fetchall()

    if productos:
        print("Productos disponibles:")
        for producto in productos:
            print(producto[0])
    else:
        print("No hay productos disponibles.")

    cursor.close()

# Función para consultar los precios de los productos
def consultar_precios():
    producto = input("Ingrese el nombre del producto: ")

    cursor = conexion.cursor()
    cursor.execute("SELECT precio FROM productos WHERE nombre = %s", (producto,))
    precio = cursor.fetchone()

    if precio:
        print(f"Precio de {producto}: {precio[0]}")
    else:
        print("El producto no existe.")

    cursor.close()

# Función para consultar los pedidos ingresados
def consultar_pedidos():
    cursor = conexion.cursor()
    cursor.execute("SELECT cliente, pedido, cantidad, precio_total FROM pedidos")
    pedidos = cursor.fetchall()

    if pedidos:
        print("Pedidos ingresados:")
        for pedido in pedidos:
            cliente, producto, cantidad, precio_total = pedido
            print(f"Cliente: {cliente}, Producto: {producto}, Cantidad: {cantidad}, Precio Total: {precio_total}")
    else:
        print("No hay pedidos ingresados.")

    cursor.close()

# Bucle principal del programa
while True:
    print("----- Menú Principal -----")
    print("1. Ingresar Pedido")
    print("2. Consultar Productos Disponibles")
    print("3. Consultar Precios")
    print("4. Consultar Pedidos")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        ingresar_pedido()
    elif opcion == "2":
        consultar_productos()
    elif opcion == "3":
        consultar_precios()
    elif opcion == "4":
        consultar_pedidos()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

# Cierre de la conexión a la base de datos
conexion.close()