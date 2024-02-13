import streamlit as st

# Título e introducción
st.title("App de Análisis de Accidentes de Tráfico")
st.markdown("***")
st.write("¡Bienvenido a la App de Análisis de Accidentes de Tráfico! Esta aplicación proporciona información y análisis sobre los accidentes de tráfico.")

# Barra lateral

st.image("https://cdn.motor1.com/images/mgl/mMANEv/s1/seguridad-vial-en-argentina-2021.-foto-telam.jpg", caption="Fuente: Telam")


import streamlit as st

# Título e introducción
st.title("Dashboard de Power BI")

# Insertar el dashboard de Power BI utilizando un iframe
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiOWVkYjFhYmUtNjI5Mi00ZmIyLTgyYTItNjcyYzU0Yzg0MWU4IiwidCI6IjgyZDEwOTAwLWM2M2ItNDhhYi1hYTg1LWViMWM2OTJjYThmMSIsImMiOjR9",
                        width=800,
                        height=600)
