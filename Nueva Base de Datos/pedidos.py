import mysql.connector
from conexion import *
from entidades import *
from CRUD import *

class Pedido:
    def __init__(self, connection):
        self.connection = connection
        self.precio_total_pedido = 0

    def registrar_pedido(self):
        cursor = self.connection.connection.cursor()
        CRUD_Select.select_productos(self.connection)
        cliente = input("Ingrese el nombre del cliente: ")
        
        productos_pedido = []
        
        while True:
            nombreproducto = input("Ingrese el producto a agregar al pedido (o '0' para finalizar): ")
            if nombreproducto == '0':
                break
            cantidad = int(input("Ingrese la cantidad deseada: "))

            try:
                cursor = self.connection.connection.cursor()
                query = "SELECT * FROM productos WHERE Nombre = %s"
                cursor.execute(query, (nombreproducto,))
                producto = cursor.fetchone()

                if producto is None:
                    print("El producto ingresado no existe. Intente nuevamente.")
                else:
                    nombre_producto = producto[1]
                    precio_producto = producto[3]
                    total_producto = precio_producto * cantidad
                    self.precio_total_pedido += total_producto

                    productos_pedido.append(f"{cantidad} x {nombre_producto} (${precio_producto} c/u) = ${total_producto}")
            except mysql.connector.Error as err:
                print("Error al consultar el producto:", err)

        if len(productos_pedido) > 0:
            productos_pedido_str = ', '.join(productos_pedido)

            try:
                cursor = self.connection.connection.cursor()
                query = "INSERT INTO pedidos (cliente, Productos, Precio) VALUES (%s, %s, %s)"
                values = (cliente, productos_pedido_str, self.precio_total_pedido)
                cursor.execute(query, values)
                self.connection.connection.commit()
                print("Pedido registrado exitosamente.")
                print(f"Precio total del pedido: ${self.precio_total_pedido}")
            except mysql.connector.Error as err:
                print("Error al registrar el pedido:", err)
        else:
            print("No se han agregado productos al pedido.")

    def obtener_precio_total_pedido(self):
        return self.precio_total_pedido
