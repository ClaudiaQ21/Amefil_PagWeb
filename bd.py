import pymysql
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv(dotenv_path='.env')

def obtener_conexion():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),         # Leer host desde .env
        port=int(os.getenv('DB_PORT', 3306)),  # Establecer un valor por defecto
        user=os.getenv('DB_USER'),         # Leer usuario desde .env
        password=os.getenv('DB_PASSWORD'), # Leer contraseña desde .env
        db=os.getenv('DB_NAME')            # Leer base de datos desde .env
    )
