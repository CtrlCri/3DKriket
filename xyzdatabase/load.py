import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def consulta(host, user, password, dbname, sql):
    # establecer conexión a la base de datos
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=dbname
    )

    # crear cursor
    cursor = conn.cursor()

    # ejecutar consulta SQL
    cursor.execute(sql)

    # obtener resultados
    resultados = cursor.fetchall()

    # imprimir resultados
    print(resultados)

    # cerrar cursor y conexión
    cursor.close()
    conn.close()

if __name__ == '__main__':
    consulta(
        host="localhost", 
        user=os.getenv('DATABASE_USER'), 
        password=os.getenv('DATABASE_PASS'), 
        dbname=os.getenv('DATABASE_NAME'), 
        sql="SELECT * FROM users_user")
