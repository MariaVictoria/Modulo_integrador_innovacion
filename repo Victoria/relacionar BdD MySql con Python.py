#istalamos la libreria
import mysql.connector

#relacionar BdD MySql con Python
#new file - python
#define una clase que es la llamada a la base de datos

  #definimos la clase
#partes :1) definicion, 2) Constructor (inicia en memoria la clase), 3) atributos y metodos
#primero definimos 

#si necesitamos instalar : en la temrinal pip install mysql-connector

class Conectar_a_Base_de_Datos():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host= 'localhost',
                port = 3306,
                user= 'root',
                password= '******',
                db = 'DER_BIG_BREAD'
            )

        except mysql.connector.Error as descripcionError:
            print ('¡No se conectó la base de datos!', descripcionError)

#esto es el bloque de conexión try/except , dentro tenenemos un objeto de conexion
# ahora el bloque del método

