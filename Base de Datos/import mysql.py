import mysql.connector
#conecto a la bbdd
class DatabaseConnection:
    def __init__(self, host, user, password, port, database, auth_plugin='mysql_native_password'):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.auth_plugin = auth_plugin
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database,
                auth_plugin=self.auth_plugin
            )
            print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos:", error)

#creamos tablas
    def create_tables(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Pedidos (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(50),
                pedido VARCHAR(255),
                precio FLOAT
            )
            """)
            print("Tablas creadas exitosamente")
        except mysql.connector.Error as err:
            print("Error al crear las tablas:", err)

#eliminamos tablas
    def drop_table(self, tabla_a_eliminar):
        cursor = self.connection.cursor()
        sentencia_sql = f"DROP TABLE IF EXISTS {tabla_a_eliminar}"
        cursor.execute(sentencia_sql)
        print(f"Tabla {tabla_a_eliminar} eliminada exitosamente.")
   
#insertamos datos las tablas
    def insert_pedido(self, nombre, pedido, precio):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Pedidos (nombre, pedido, precio) VALUES (%s, %s, %s)"
            values = (nombre, pedido, precio)
            cursor.execute(query, values)
            self.connection.commit()
            print("Pedido agregado exitosamente.")
        except mysql.connector.Error as err:
            print("Error al insertar pedido:", err)

#cerramos conexion
    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

# Crear una instancia de DatabaseConnection
db_connection = DatabaseConnection(
    host="localhost",
    user="root",
    password="******",
    port="3306",
    database="BigBread"
)

db_connection.connect()

db_connection = DatabaseConnection(
    host="localhost",
    user="root",
    password="Tomas071",
    port="3306",
    database="BigBread"
)

db_connection.connect()

# Eliminar las tablas
db_connection.drop_table("tabla2") 
db_connection.drop_table("tabla1") 
db_connection.drop_table("Ingredientes_Produccion") 
db_connection.drop_table("Produccion") 

# Crear las tablas
db_connection.create_tables()

# Cerrar la conexión
db_connection.close()

