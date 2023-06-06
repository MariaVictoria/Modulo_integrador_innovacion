
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
            print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos:", error)

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


db_connection.close()
