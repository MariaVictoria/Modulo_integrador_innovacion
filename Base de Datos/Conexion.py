import mysql.connector

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
            cursor = self.connection.cursor()
            print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos:", error)

    def create_tables(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedidos (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(50),
                pedido VARCHAR(255),
                precio FLOAT
            )
        """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS tabla2 (
                id INT PRIMARY KEY AUTO_INCREMENT,
                ciudad VARCHAR(50),
                pais VARCHAR(50)
            )
        """)
            print("Tablas creadas exitosamente")
        except mysql.connector.Error as err:
            print("Error al crear las tablas:", err)

    def drop_table(self, tabla_a_eliminar):
        cursor = self.connection.cursor()
        sentencia_sql = f"DROP TABLE IF EXISTS {tabla_a_eliminar}"
        cursor.execute(sentencia_sql)
        print(f"Tabla {tabla_a_eliminar} eliminada exitosamente.")
        

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")


db_connection = DatabaseConnection(
    host="localhost",
    user="root",
    password="kali",
    port="3306",
    database="BigBread"
)
db_connection.connect()


db_connection.drop_table("tabla2") 
db_connection.drop_table("tabla1") 

db_connection.close()


