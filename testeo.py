import pandas as pd
import snowflake.connector
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

# URL del archivo Parquet
ruta_archivo = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{nombre_archivo}"

# Intentar cargar el archivo Parquet en un DataFrame
df = pd.read_parquet(ruta_archivo)
print(f"DataFrame cargado correctamente desde {ruta_archivo}")


# Establecer la conexión con Snowflake
conn = snowflake.connector.connect(
    user='ELIASALMADA1234',
    password='Ichi2017',
    account='pzbgdyt-aib83585',
    warehouse='COMPUTE_WH',
    database='TEST',
    schema='PUBLIC'
)

# Crear un cursor
cursor = conn.cursor()

# Nombre de la tabla en Snowflake
table_name = "taxis"



# Insertar los datos en la tabla
for _, row in df.iterrows():
    insert_query = f"""
    INSERT INTO {table_name} 
    VALUES ({row['VendorID']}, '{row['tpep_pickup_datetime']}', '{row['tpep_dropoff_datetime']}', 
            {row['passenger_count']}, {row['trip_distance']}, {row['RatecodeID']}, '{row['store_and_fwd_flag']}', 
            {row['PULocationID']}, {row['DOLocationID']}, {row['payment_type']}, {row['fare_amount']}, 
            {row['extra']}, {row['mta_tax']}, {row['tip_amount']}, {row['tolls_amount']}, 
            {row['improvement_surcharge']}, {row['total_amount']}, {row['congestion_surcharge']}, 
            {row['Airport_fee']})
    """
    cursor.execute(insert_query)

# Confirmar la ejecución de la transacción
conn.commit()

# Imprimir el progreso
print(f"Se han cargado {len(df)} filas en la tabla {table_name}.")

# Cerrar el cursor y la conexión
cursor.close()
conn.close()
