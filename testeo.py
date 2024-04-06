import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from datetime import datetime

# Obtener la fecha actual
fecha_actual = datetime.now()

# Calcular el mes y año tres meses atrás
mes_tres_meses_atras = fecha_actual.month - 3
año_tres_meses_atras = fecha_actual.year
if mes_tres_meses_atras <= 0:
    mes_tres_meses_atras += 12
    año_tres_meses_atras -= 1

# Construir el nombre del archivo Parquet
nombre_archivo = f"yellow_tripdata_{año_tres_meses_atras}-{mes_tres_meses_atras:02}.parquet"

# Construir la ruta del archivo Parquet
ruta_archivo = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{nombre_archivo}"

# Intentar cargar el archivo Parquet en un DataFrame
df = pd.read_parquet(ruta_archivo)
print(f"DataFrame cargado correctamente desde {ruta_archivo}")

# Crear una conexión a la base de datos
conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    port=port
)

# Nombre de la tabla en PostgreSQL
table_name = "testeo9"

# Crear un cursor
cur = conn.cursor()



# Crear una lista de tuplas con los datos
data = [tuple(row) for _, row in df.iterrows()]

# Insertar los datos en la tabla
execute_values(cur, f"INSERT INTO {table_name} VALUES %s", data)

# Confirmar la ejecución de la transacción
conn.commit()

# Imprimir el progreso
print(f"Se han cargado {len(data)} filas en la tabla {table_name}.")

# Cerrar el cursor y la conexión
cur.close()
conn.close()
