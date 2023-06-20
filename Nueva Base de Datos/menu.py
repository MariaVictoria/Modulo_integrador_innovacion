from entidades import Ingredientes, Productos, Pedidos
import mysql.connector
from conexion import DatabaseConnection

class MenuInteraccion:
    def __init__(self):
        # Inicializar la conexión con la base de datos
        self.db_connection = DatabaseConnection(
            host="localhost",
            user="root",
            password="Delfines/2",
            port="3306",
            database="Sandwiches_BigBread"
        )
        self.db_connection.connect()

    def mostrar_menu(self):
        num_pedidos = 0  # Variable para almacenar el número de pedidos

        while True:
            print("****** SISTEMA DE REGISTRO DE PEDIDOS ******")
            print("=== MENÚ ===")
            print("1. Ver productos")
            print("2. Agregar productos")
            print("3. Actualizar productos")
            print("4. Eliminar producto")
            print("5. Registrar pedido")
            print("6. Salir")

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                self.ver_productos()
            elif opcion == "2":
                self.agregar_producto()
            elif opcion == "3":
                self.actualizar_producto()
            elif opcion == "4":
                self.eliminar_producto()
            elif opcion == "5":
                self.registrar_pedido(num_pedidos)
                num_pedidos += 1
            elif opcion == "6":
                print("****** USTED HA SALIDO DEL SISTEMA DE REGISTRO DE PEDIDOS ******")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def ver_productos(self):
        # Lógica para consultar y mostrar los productos en la base de datos
        cursor = self.db_connection.connection.cursor()
        query = "SELECT * FROM Productos"
        cursor.execute(query)
        productos = cursor.fetchall()

        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print("Productos:")
            for producto in productos:
                print(producto)

    def agregar_producto(self):
        # Lógica para agregar un nuevo producto a la base de datos
        id_productos = int(input("Ingrese el ID del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        ingredientes = input("Ingrese los ingredientes del producto: ")

        # Crear un objeto Productos
        producto = Productos(id_productos, nombre, ingredientes, precio)

        try:
            # Lógica para agregar el objeto producto a la base de datos o realizar otras operaciones necesarias
            # ...
            print("Producto agregado exitosamente.")
        except mysql.connector.Error as err:
            print("Error al insertar producto:", err)

    def actualizar_producto(self):
        # Lógica para actualizar un producto existente en la base de datos
        id_producto = int(input("Ingrese el ID del producto a actualizar: "))
        nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
        nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))

        try:
            cursor = self.db_connection.connection.cursor()
            query = "UPDATE Productos SET Nombre = %s, Precio = %s WHERE idProductos = %s"
            values = (nuevo_nombre, nuevo_precio, id_producto)
            cursor.execute(query, values)
            self.db_connection.connection.commit()
            print("Producto actualizado exitosamente.")
        except mysql.connector.Error as err:
            print("Error al actualizar producto:", err)

    def eliminar_producto(self):
        # Lógica para eliminar un producto de la base de datos
        id_producto = int(input("Ingrese el ID del producto a eliminar: "))

        try:
            cursor = self.db_connection.connection.cursor()
            query = "DELETE FROM Productos WHERE idProductos = %s"
            values = (id_producto,)
            cursor.execute(query, values)
            self.db_connection.connection.commit()
            print("Producto eliminado exitosamente.")
        except mysql.connector.Error as err:
            print("Error al eliminar producto:", err)

    def registrar_pedido(self, num_pedidos):
        # Lógica para registrar un nuevo pedido en la base de datos
        id_pedido = num_pedidos + 1
        cliente = input("Ingrese el nombre del cliente: ")
        id_productos = input("Ingrese los IDs de los productos separados por comas: ").split(",")
        productos = []

        # Obtener los objetos Productos correspondientes a los IDs ingresados
        cursor = self.db_connection.connection.cursor()
        query = "SELECT * FROM Productos WHERE idProductos IN (%s)" % ','.join(['%s'] * len(id_productos))
        cursor.execute(query, id_productos)
        productos_data = cursor.fetchall()

        for producto_data in productos_data:
            id_producto = producto_data[0]
            nombre = producto_data[1]
            ingredientes = producto_data[2]
            precio = producto_data[3]
            producto = Productos(id_producto, nombre, ingredientes, precio)
            productos.append(producto)

        # Calcular el precio total del pedido
        precio_total = sum(producto.obtener_precio() for producto in productos)

        # Crear un objeto Pedidos
        pedido = Pedidos(id_pedido, cliente, productos, precio_total, id_productos)

        try:
            # Lógica para agregar el objeto pedido a la base de datos o realizar otras operaciones necesarias
            # ...
            print("Pedido registrado exitosamente.")
        except mysql.connector.Error as err:
            print("Error al registrar pedido:", err)


# Crear una instancia de la clase MenuInteraccion y mostrar el menú
menu = MenuInteraccion()
menu.mostrar_menu()
