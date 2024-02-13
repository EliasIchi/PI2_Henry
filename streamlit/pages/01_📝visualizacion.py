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
