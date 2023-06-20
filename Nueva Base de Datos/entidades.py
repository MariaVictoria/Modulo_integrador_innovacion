import mysql.connector

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
                database=self.database
            )
            print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as error:
            print("No se pudo establecer la conexión: {}".format(error))

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

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

class Productos:
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
