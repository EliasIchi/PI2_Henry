import streamlit as st

# Título e introducción
st.title("Dashboard de Power BI")
st.markdown("***")


# Insertar el dashboard de Power BI utilizando un iframe
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiOWVkYjFhYmUtNjI5Mi00ZmIyLTgyYTItNjcyYzU0Yzg0MWU4IiwidCI6IjgyZDEwOTAwLWM2M2ItNDhhYi1hYTg1LWViMWM2OTJjYThmMSIsImMiOjR9",
                        width=800,
                        height=600)
