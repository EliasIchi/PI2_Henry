import pandas as pd
import psycopg2
from datetime import datetime, timedelta

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

# Detalles de la conexión a PostgreSQL
host = "bivcrdepa3dc6zn6enju-postgresql.services.clever-cloud.com"
database = "bivcrdepa3dc6zn6enju"
user = "uyomkpixi8ntfsmrgzgi"
password = "F2kDStOnYq4NGphr65HyLtudOh63rq"
port = "50013"


# Intentar cargar el archivo Parquet en un DataFrame
try:
    df = pd.read_parquet(ruta_archivo)
    print(f"DataFrame cargado correctamente desde {ruta_archivo}")
except Exception as e:
    print(f"No se pudo cargar el archivo {nombre_archivo}: {e}")

# Establecer conexión a PostgreSQL
conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    port=port
)

# Nombre de la tabla en PostgreSQL
table_name = "testeo"

df = df[['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime',
       'trip_distance']]

total_filas = len(df)

cur = conn.cursor()

# Iterar sobre las filas del DataFrame y ejecutar INSERT INTO para cada fila
for index, row in df.iterrows():
    try:
        cur.execute("""
        INSERT INTO testeo (
            VendorID, tpep_pickup_datetime, tpep_dropoff_datetime, trip_distance)
        VALUES (%s, %s, %s, %s)
        """, tuple(row))
        
        # Mostrar el progreso
        print(f"Fila {index + 1}/{total_filas} cargada en la tabla en PostgreSQL.")
    except Exception as e:
        print(f"Error al insertar fila {index + 1}: {e}")
        conn.rollback()  # Revertir cambios en caso de error
        break

# Confirmar la ejecución de la transacción
conn.commit()

# Cerrar el cursor y la conexión
cur.close()
conn.close()

