import Conexion

from Conexion import pedidos

print("****** SISTEMA DE REGISTRO DE PEDIDOS ******")

while True:
    dato = int(input('Desea ingresar los datos requeridos para registrar su pedido? Presione 1 para continuar, X para salir ').lower())

if dato == X: 
    print ('****** USTED A SALIDO DEL SISTEMA DE REGISTRO DE PEDIDOS ****** ')
    exit
elif dato == 1:
    con = conexion.BaseDeDatos()
    idproducto = int(input("ingresa el codigo"))
    nombre = input("ingresa el nombre del producto")
    descripcion = input("producto")
    precio = int(input("ingrese el precio"))
    idingredientes = int(input("ingrese codigo de ingredintes"))

    datos = Productos(idproducto, nombre, descripcion, precio, idingredientes)
    con.insertar_productos(datos)
elif dato == 2:
    cone = conexion.BaseDeDatos()
    conee = cone.Listado_De_Productos()
    for i in conee:
        print("id producto: " , i[0] , "Nombre: " , i[1] , "Descripcion" , i[2], "Precio: " , i[3] , "id ingredientes" , i[4])
