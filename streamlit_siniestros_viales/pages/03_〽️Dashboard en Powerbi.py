import streamlit as st

# Título e introducción
st.title("Dashboard de Power BI")
st.markdown("***")


# Insertar el dashboard de Power BI utilizando un iframe
st.components.v1.iframe("https://app.powerbi.com/reportEmbed?reportId=65cb74ba-89c1-4087-b879-251dca92e239&autoAuth=true&ctid=82d10900-c63b-48ab-aa85-eb1c692ca8f1")
