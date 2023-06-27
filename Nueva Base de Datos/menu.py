from entidades import Ingredientes, Productos, Pedidos
import mysql.connector
from conexion import *
from CRUD import *


class MenuInteraccion:
    def __init__(self, connection):
        self.connection = connection

    def mostrar_menu(self):
        num_pedidos = 0

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
        cursor = self.connection.connection.cursor()
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
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        ingredientes = input("Ingrese los ingredientes del producto: ")

        CRUD.insert_Productos(self.connection, nombre, ingredientes, precio)

    def actualizar_producto(self):
        cursor = self.connection.connection.cursor()
        query = "SELECT * FROM Productos"
        cursor.execute(query)
        productos = cursor.fetchall()

        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print("Productos:")
            for producto in productos:
                print(producto)

            idProducto = input("Ingrese el ID del producto a actualizar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
            nuevos_ingredientes = input("Ingrese los nuevos ingredientes del producto: ")


            try:
                cursor = self.connection.connection.cursor()
                query = "UPDATE Productos SET Nombre = %s, Precio = %s WHERE idProductos = %s"
                values = (nuevo_nombre, nuevo_precio, idProducto)
                cursor.execute(query, values)
                self.connection.connection.commit()
                print("Producto actualizado exitosamente.")
            except mysql.connector.Error as err:
                print("Error al actualizar producto:", err)

    def eliminar_producto(self):
        cursor = self.connection.connection.cursor()
        query = "SELECT * FROM Productos"
        cursor.execute(query)
        productos = cursor.fetchall()

        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print("Productos:")
            for producto in productos:
                print(producto)

            idProducto = input("Ingrese el ID del producto a eliminar: ")

            try:
                cursor = self.connection.connection.cursor()
                query = "DELETE FROM Productos WHERE idProductos = %s"
                values = (idProducto,)
                cursor.execute(query, values)
                self.connection.connection.commit()
                print("Producto eliminado exitosamente.")
            except mysql.connector.Error as err:
                print("Error al eliminar producto:", err)

    def registrar_pedido(self, num_pedidos):
        cursor = self.connection.connection.cursor()
        query = "SELECT * FROM Productos"
        cursor.execute(query)
        productos = cursor.fetchall()

        if len(productos) == 0:
            print("No hay productos registrados.")
            return

        print("Productos:")
        for producto in productos:
            print(producto)

        cliente = input("Ingrese el nombre del cliente: ")

        productos_pedido = []
        precio_total_pedido = 0

        while True:
            idProducto = input("Ingrese el ID del producto a agregar al pedido (o '0' para finalizar): ")
            if idProducto == '0':
                break
            cantidad = int(input("Ingrese la cantidad del producto: "))

            try:
                cursor = self.connection.connection.cursor()
                query = "SELECT * FROM Productos WHERE idProductos = %s"
                values = (idProducto,)
                cursor.execute(query, values)
                producto = cursor.fetchone()

                if producto is not None:
                    precio_unitario = producto[3]
                    precio_total_producto = precio_unitario * cantidad

                    productos_pedido.append((producto[1], precio_total_producto, idProducto, cantidad))
                    precio_total_pedido += precio_total_producto

                    print("Producto agregado al pedido.")
                    print("Precio total del producto:", precio_total_producto)
                else:
                    print("No existe un producto con el ID proporcionado.")
            except mysql.connector.Error as err:
                print("Error al registrar pedido:", err)

        if not productos_pedido:
            print("No se han agregado productos al pedido.")
            return

        try:
            cursor = self.connection.connection.cursor()
            query = "INSERT INTO Pedidos (cliente, Productos, Precio, idProductos, cantidad) VALUES (%s, %s, %s, %s, %s)"
            productos_nombres = [p[0] for p in productos_pedido]
            productos_precios = [p[1] for p in productos_pedido]
            productos_ids = [p[2] for p in productos_pedido]
            productos_cantidades = [p[3] for p in productos_pedido]
            values = (cliente, str(productos_nombres), precio_total_pedido, str(productos_ids), str(productos_cantidades))
            cursor.execute(query, values)
            self.connection.connection.commit()

            print("Pedido registrado exitosamente.")
            print("Precio total del pedido:", precio_total_pedido)
        except mysql.connector.Error as err:
            print("Error al registrar pedido:", err)




# Creación de la instancia de conexión a la base de datos

connection.connect()

# Creación de la instancia del menú de interacción
menu = MenuInteraccion(connection)
menu.mostrar_menu()

# Cierre de la conexión a la base de datos
connection.close()