import mysql.connector
from conexion import *
from entidades import *
from CRUD import *
from pedidos import *
import time

#*****************MENU********************
class Menu:
    def __init__(self, connection):
        self.connection = connection

    def mostrar_menu(self):
        num_pedidos = 0

        while True:
            print('\n****** SISTEMA DE REGISTRO DE "BigBred" ******\n')
            print("=============== MENÚ ===================")
            print("=== A continuación ingrese la opción elegida ===")
            time.sleep(1)
            print("\n1. Ver listado de Sandwiches")  # CRUD select
            time.sleep(1)
            print("\n2. Agregar Sandwiches al listado ")  # CRUD insert
            time.sleep(1)
            print("\n3. Actualizar precio a Sandwiches del listado ")  # CRUD update
            time.sleep(1)
            print("\n4. Eliminar Sandwiches del listado ")  # CRUD delete
            time.sleep(1)
            print("\n5. Ver Ingredientes de los Sandwiches")  # CRUD select
            time.sleep(1)
            print("\n6. Agregar Ingredientes para nuevos Sandwiches")  # CRUD insert
            time.sleep(1)
            print("\n7. Actualizar Ingredientes de los Sandwiches")  # CRUD update
            time.sleep(1)
            print("\n8. Eliminar Ingredientes del listado")  # CRUD delete
            time.sleep(1)
            print("\n9. Registrar un nuevo pedido de Sandwiches")
            time.sleep(1)
            print("\n10. Revisar precio del pedido")
            time.sleep(1)
            print("\n11. Revisar cantidad de pedidos cargados.")
            time.sleep(1)
            print("\n0. Salir\n")

            opcion = input("Ingrese una opción: \n")

            if opcion == "1":
                CRUD_Select.select_productos(self.connection)
                time.sleep(1)
            elif opcion == "2":
                nombre = input("Ingrese el nombre del nuevo Sandwich: ")
                time.sleep(1)
                ingredientes = input(f"Ingrese los ingredientes del nuevo Sandwich {nombre}: ")
                time.sleep(1)
                precio = float(input(f"Ingrese el precio del nuevo Sandwich {nombre}: $"))
                time.sleep(1)
                print(f'Sandwich agregado con éxito : ')
                time.sleep(1)
                CRUD_Insert.insert_productos(self.connection, nombre, ingredientes, precio)
                time.sleep(1)
                CRUD_Select.select_productos(self.connection)
                time.sleep(1)
            elif opcion == "3":
                CRUD_Select.select_productos(self.connection)
                nombre = input("Ingrese el nombre del Sandwich al cual quiere actualizar el precio: ")
                time.sleep(1)
                precio = float(input(f"Ingrese el nuevo precio del Sandwich {nombre}: "))
                time.sleep(1)
                print(f'Actualización realizada con éxito : ')
                time.sleep(1)
                CRUD_Update.update_producto(self.connection, nombre, precio)
                time.sleep(1)
                CRUD_Select.select_productos(self.connection)
                time.sleep(1)
            elif opcion == "4":
                CRUD_Select.select_productos(self.connection)
                nombre = input("Ingrese el nombre del Sandwich a eliminar: ")
                time.sleep(1)
                CRUD_Delete.delete_productos(self.connection, nombre)
                time.sleep(1)
            elif opcion == "5":
                CRUD_Select.select_ingredientes(self.connection)
                time.sleep(1)
            elif opcion == "6":
                nombre = input("Ingrese el nombre del ingrediente a agregar: ")
                time.sleep(1)
                CRUD_Insert.insert_ingredientes(self.connection, nombre)
                print(f'Ingrediente agregado con éxito : ')
                time.sleep(1)
                CRUD_Select.select_ingredientes(self.connection)
                time.sleep(1)
            elif opcion == "7":
                nombre = input("Ingrese el nombre del ingrediente a actualizar: ")
                time.sleep(1)
                precio = float(input("Ingrese el nuevo precio del ingrediente: "))
                time.sleep(1)
                print(f'Actualizacion exitosa : ')
                time.sleep(1)
                CRUD_Update.update_ingrediente(self.connection, nombre, precio)
                time.sleep(1)
                CRUD_Select.select_ingredientes(self.connection)
                time.sleep(1)
            elif opcion == "8":
                nombre = input("Ingrese el nombre del ingrediente a eliminar: ")
                time.sleep(1)
                print(f'Actualizacion exitosa : ')
                time.sleep(1)
                CRUD_Delete.delete_ingrediente(self.connection, nombre)
                time.sleep(1)
                CRUD_Select.select_ingredientes(self.connection)
                time.sleep(1)
            elif opcion == "9":
                pedido = Pedido(self.connection)
                pedido.registrar_pedido()
                num_pedidos += 1
            elif opcion == "10":
                pedido = Pedido(self.connection)
                precio_total_pedido = pedido.obtener_precio_total_pedido()
                print(f"El precio final a abonar por el pedido registrado es de: ${precio_total_pedido}")
            elif opcion == "11":
                print(f"La cantidad de pedidos registrados: {num_pedidos}")
                time.sleep(1)
            elif opcion == "0":
                print("\n****** USTED HA SALIDO DEL SISTEMA DE REGISTRO DE PEDIDOS ******\n")
                time.sleep(1)
                break
            else:
                print(f"\n{opcion} No es una opción válida. Intente nuevamente.\n")
                time.sleep(1)

# Establecer la conexión a la base de datos
connection.connect()

# Crear objeto del menú y mostrarlo
menu = Menu(connection)
menu.mostrar_menu()

# Cerrar la conexión a la base de datos
connection.close()