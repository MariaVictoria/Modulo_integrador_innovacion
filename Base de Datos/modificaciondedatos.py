import mysql.connector
# Configura los detalles de conexión a la base de datos
tabla = 'Ingredientes_Produccion'
consulta = f"DELETE FROM {Ingredientes_Produccion}"

# Ejecuta la consulta
cursor.execute(consulta)

# Guarda los cambios
conexion.commit()
