import mysql.connector

#*****************CONEXION/CIERRE********************
class DatabaseConnection:
    def __init__(self, host, user, password, port, database): 
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.connection = None 

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port, 
                database=self.database,
            )
        except mysql.connector.Error as error:
            print("No se pudo establecer la conexión: {}".format(error))

    def close(self):
        if self.connection:
            self.connection.close()

#*****************ENTIDADES********************
class Ingredientes:
    def __init__(self, idIngredientes, Nombre):
        self._idIngredientes = idIngredientes
        self._Nombre =  Nombre

    @property
    def idIngredientes(self):
        return self._idIngredientes

    @property
    def Nombre(self):
        return self._Nombre
    
    @Nombre.setter
    def Nombre(self, Nombre):
        self._Nombre = Nombre

    def mostrar_detalle(self):
        print(f"Ingrediente: {self._Nombre}")

    def __str__(self):
        return f"Ingrediente ID: {self._idIngredientes}, Ingrediente: {self._Nombre}"

class Producto:
    def __init__(self, idProductos, Nombre, Ingredientes, Precio):
        self._idProductos = idProductos
        self._Nombre = Nombre
        self._Ingredientes = Ingredientes
        self._Precio = Precio

    @property
    def idProductos(self):
        return self._idProductos

    @property
    def Nombre(self):
        return self._Nombre

    @property
    def Ingredientes(self):
        return self._Ingredientes

    @Ingredientes.setter
    def Ingredientes(self, Ingredientes):
        self._Ingredientes = Ingredientes

    @property
    def Precio(self):
        return self._Precio

    @Precio.setter
    def Precio(self, Precio):
        self._Precio = Precio

    def mostrar_detalle(self):
        print(f"Producto: {self._Nombre}")

    def __str__(self):
        return f"Producto ID: {self._idProductos}, Producto: {self._Nombre}"

    def mostrar_Ingredientes(self):
        print(f'Ingredientes: {self._Ingredientes}')

    def obtener_precio(self):
        return self._Precio

class Pedidos:
    def __init__(self, idPedidos, cliente, Productos, Precio, idProductos):
        self._idPedidos = idPedidos
        self._cliente = cliente
        self._Productos = Productos
        self._Precio = Precio
        self._idProductos = idProductos

    @property
    def idPedidos(self):
        return self._idPedidos

    @property
    def cliente(self):
        return self._cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @property
    def Productos(self):
        return self._Productos
    
    @Productos.setter
    def Productos(self, Productos):
        self._Productos = Productos

    @property
    def Precio(self):
        return self._Precio

    @property
    def idProductos(self):
        return self._idProductos
    
#*****************CRUD********************
class CRUD:
    @staticmethod
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

    @staticmethod
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

#*****************MENU********************
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



# Configuración de la conexión a la base de datos
host = "localhost"
user = "root"
password = "Delfines/2"
port = "3306"
database = "Sandwiches_BigBread"

# Creación de la instancia de conexión a la base de datos
connection = DatabaseConnection(host, user, password, port, database)
connection.connect()

# Creación de la instancia del menú de interacción
menu = MenuInteraccion(connection)
menu.mostrar_menu()

# Cierre de la conexión a la base de datos
connection.close()