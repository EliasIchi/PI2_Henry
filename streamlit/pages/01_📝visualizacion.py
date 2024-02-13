import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import geopandas as gpd
import folium

if st.checkbox("Mostrar texto"):
    st.write("hola")



# URLs de los libros de Excel
url_homicidios = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/victimas-siniestros-viales/homicidios.xlsx"

xls_homicidios = pd.ExcelFile(url_homicidios)

# Obtener nombres de las hojas y cantidad de hojas
nombres_hojas_homicidios = xls_homicidios.sheet_names

h_hechos = df_homicidios_primera_hoja = pd.read_excel(url_homicidios, sheet_name=nombres_hojas_homicidios[0])

if st.checkbox("Mostrar dataset"):
    st.write(h_hechos)


# Calcular día, mes y año
h_hechos['FECHA'] = pd.to_datetime(h_hechos['FECHA'])
h_hechos['Dia'] = h_hechos['FECHA'].dt.day
h_hechos['Mes'] = h_hechos['FECHA'].dt.month
h_hechos['Año'] = h_hechos['FECHA'].dt.year

# Obtener los años únicos para el widget de selección
años_únicos = h_hechos['Año'].unique()

# Widget de selección para el año
año_seleccionado = st.selectbox("Selecciona un año:", años_únicos)

# Filtrar los datos por el año seleccionado
datos_año_seleccionado = h_hechos[h_hechos['Año'] == año_seleccionado]

# Configurar el tamaño de la figura
plt.figure(figsize=(10, 6))

# Graficar por día para el año seleccionado
datos_por_dia = datos_año_seleccionado.groupby('Dia')['N_VICTIMAS'].sum()
plt.bar(datos_por_dia.index, datos_por_dia.values, color="#500500")
plt.title(f'Distribución de víctimas por día en el año {año_seleccionado}')
plt.xlabel('Día del mes')
plt.ylabel('Cantidad de víctimas')
plt.xticks(np.arange(1, 32))  # Mostrar todos los días en el eje x

# Mostrar el gráfico
st.pyplot(plt)


# Agrupar por la columna 'VICTIMA' y contar las ocurrencias
victima_counts = h_hechos['N_VICTIMAS'].value_counts()

# Crear el gráfico de torta
plt.figure(figsize=(8, 6))
victima_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribución de víctimas')
plt.ylabel('')

# Mostrar el gráfico
plt.show()


if st.checkbox("vista head o tail"):
    if st.button("Ver head"):
        st.write(h_hechos.head())
    if st.button("Ver tail"):
        st.write(h_hechos.tail())

dim = st.radio("Dimensión a mostrar:",("Filas",'Columnas'), horizontal= True)

if dim == "Filas":
    st. write("Cantidad de filas: ", h_hechos.shape[0])
else:
    st.write("Cantidad de columnas ", h_hechos.shape[1])

import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

# Cargar el archivo GeoJSON de las comunas de Buenos Aires
mapa_caba = gpd.read_file("https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-educacion/comunas/comunas.geojson")

# Crear un nuevo DataFrame con las coordenadas limpias
h_hechos_limpios = h_hechos.dropna(subset=['pos x', 'pos y'])
h_hechos_limpios = h_hechos_limpios[(h_hechos_limpios['pos x'] != '.') & (h_hechos_limpios['pos y'] != '.')]

# Convertir las coordenadas a formato numérico
h_hechos_limpios['pos x'] = pd.to_numeric(h_hechos_limpios['pos x'])
h_hechos_limpios['pos y'] = pd.to_numeric(h_hechos_limpios['pos y'])

# Crear un gráfico utilizando Matplotlib
fig, ax = plt.subplots(figsize=(10, 10))

# Superponer los puntos del DataFrame "h_hechos_limpios"
ax.scatter(h_hechos_limpios['pos x'], h_hechos_limpios['pos y'], color='red', alpha=0.5, s=5)

# Añadir el mapa base estilo OpenStreetMap
ctx.add_basemap(ax, crs=mapa_caba.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik)

# Establecer título y etiquetas de ejes
ax.set_title('Mapa de la Ciudad Autónoma de Buenos Aires con puntos')
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')

# Mostrar el mapa
plt.show()

