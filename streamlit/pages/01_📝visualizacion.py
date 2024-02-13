import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título e introducción
st.title("Visualización de Datos de Accidentes de Tráfico")
st.markdown("En esta sección, se presentan visualizaciones y análisis de datos relacionados con los accidentes de tráfico.")

# Cargar los datos
url_homicidios = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/victimas-siniestros-viales/homicidios.xlsx"
h_hechos = pd.read_excel(url_homicidios)

# Mostrar dataset
if st.checkbox("Mostrar dataset"):
    st.write(h_hechos)

# Mostrar head o tail del dataset
if st.checkbox("Ver las primeras o últimas filas del dataset"):
    option = st.radio("Seleccione una opción:", ("Head", "Tail"))
    if option == "Head":
        st.write(h_hechos.head())
    elif option == "Tail":
        st.write(h_hechos.tail())

# Dimensión del dataset
dim = st.radio("Dimensión a mostrar:", ("Filas", "Columnas"))
if dim == "Filas":
    st.write("Cantidad de filas:", h_hechos.shape[0])
else:
    st.write("Cantidad de columnas:", h_hechos.shape[1])

# Calcular día, mes y año
h_hechos['FECHA'] = pd.to_datetime(h_hechos['FECHA'])
h_hechos['Dia'] = h_hechos['FECHA'].dt.day
h_hechos['Mes'] = h_hechos['FECHA'].dt.month
h_hechos['Año'] = h_hechos['FECHA'].dt.year


st.subheader("Cantidad de victimas por dia y por año")

# Widget de selección para el año
años_únicos = h_hechos['Año'].unique()
año_seleccionado = st.selectbox("Selecciona un año:", años_únicos)

# Filtrar los datos por el año seleccionado
datos_año_seleccionado = h_hechos[h_hechos['Año'] == año_seleccionado]

# Visualización de víctimas por día en el año seleccionado
plt.figure(figsize=(10, 6))
datos_por_dia = datos_año_seleccionado.groupby('Dia')['N_VICTIMAS'].sum()
plt.bar(datos_por_dia.index, datos_por_dia.values, color="#500500")
plt.title(f'Distribución de víctimas por día en el año {año_seleccionado}')
plt.xlabel('Día del mes')
plt.ylabel('Cantidad de víctimas')
plt.xticks(np.arange(1, 32))  # Mostrar todos los días en el eje x
st.pyplot(plt)

# Título e introducción
st.title("Visualización de Datos de Accidentes de Tráfico")
st.markdown("En esta sección, se presentan visualizaciones y análisis de datos relacionados con los accidentes de tráfico.")

# Cargar los datos
url_homicidios = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/victimas-siniestros-viales/homicidios.xlsx"
h_hechos = pd.read_excel(url_homicidios)

# Calcular día, mes y año
h_hechos['FECHA'] = pd.to_datetime(h_hechos['FECHA'])
h_hechos['Dia'] = h_hechos['FECHA'].dt.day
h_hechos['Mes'] = h_hechos['FECHA'].dt.month
h_hechos['Año'] = h_hechos['FECHA'].dt.year

# Obtener años únicos como cadenas de texto
años_únicos = h_hechos['Año'].unique().astype(str)

# Widget de selección para el año
año_seleccionado = st.selectbox("Selecciona un año:", años_únicos, key="year_selector")

# Filtrar los datos por el año seleccionado
datos_año_seleccionado = h_hechos[h_hechos['Año'] == int(año_seleccionado)]

# Visualización de víctimas por mes en el año seleccionado
plt.figure(figsize=(10, 6))
datos_por_mes = datos_año_seleccionado.groupby('Mes')['N_VICTIMAS'].sum()
plt.bar(datos_por_mes.index, datos_por_mes.values, color="#500500")
plt.title(f'Distribución de víctimas por mes en el año {año_seleccionado}')
plt.xlabel('Mes')
plt.ylabel('Cantidad de víctimas')
plt.xticks(np.arange(1, 13))  # Mostrar todos los meses en el eje x
st.pyplot(plt)




# Mapa de puntos de interés
st.subheader("Mapa de Puntos de Interés")
# Eliminar filas con valores no válidos en las columnas de coordenadas
h_hechos_limpios = h_hechos.dropna(subset=['pos x', 'pos y'])
h_hechos_limpios = h_hechos_limpios[(h_hechos_limpios['pos x'] != '.') & (h_hechos_limpios['pos y'] != '.')]
# Crear un DataFrame para los puntos de interés
puntos_interes = pd.DataFrame({
    'lat': h_hechos_limpios['pos y'],
    'lon': h_hechos_limpios['pos x'],
})
# Convertir las columnas de latitud y longitud a tipo numérico
puntos_interes['lat'] = pd.to_numeric(puntos_interes['lat'], errors='coerce')
puntos_interes['lon'] = pd.to_numeric(puntos_interes['lon'], errors='coerce')
# Mostrar el mapa en Streamlit
st.map(puntos_interes)


