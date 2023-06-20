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
   

class Productos :
    def __init__(self, idProductos, Nombre,Ingredientes,Precio):
        self._idProductos = idProductos
        self._Nombre = Nombre
        self._Ingredientes = Ingredientes
        self._Precio = Precio

    @property   
    def idProductos(self):
        return self._idProductos
    @property
    def Nombre(self):
        return self.Nombre
    @property
    def Ingredientes(self):
        return self.Ingredientes
    @Ingredientes.setter
    def Ingredientes(self,Ingredientes):
        self.Ingredientes = Ingredientes
    
    @property
    def Precio(self):
        return self.Precio
    @Precio.setter
    def Precio(self, Precio):
        self._Precio = Precio
       
    def mostrar_detalle(self):
        print(f"Producto: {self._Nombre}")

    def __str__(self):
        return f"Producto ID: {self._idProducto},Producto: {self._Nombre}"
    
    def mostrar_Ingredientes(self):
        print(f'Ingredientes: {Ingredientes}')

    def obtener_precio(self):
        return self._Precio
    
class Pedidos:
    def __init__(self,idPedidos,cliente,Productos,Precio,idProductos):
        self._idPedidos = idPedidos
        self._cliente = cliente
        self._Productos= Productos
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
