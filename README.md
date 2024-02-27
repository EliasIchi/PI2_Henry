
# <center>Siniestros Viales (CABA)<center> 🚗💥📊

¡Bienvenidos al repositorio del Proyecto Individual N°2 de la carrera *Ciencia de Datos* en *Henry*! 🎓

![accidentes_viales](https://github.com/EliasIchi/PI2_Henry/assets/124707045/797de0bd-c95a-4b1f-b9d1-a9eaa2529df1)

## Data Analyst 📊

En esta oportunidad, *Henry* nos desafía a crear un proyecto desde el rol de analista de datos, para ello, se plantean ciertos requerimientos que serán recorridos en este repositorio.

## Índice 📝

- [Contexto](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#contexto-)
- [Estructura del proyecto](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#estructura-del-proyecto-)
- [Desarrollo del proyecto](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#desarrollo-del-proyecto-)
- [EDA (Exploratory Data Analysis)](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#eda-exploratory-data-analysis-)
- [ETL (Extract, Transform, Load)](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#etl-extract-transform-load-)
- [KPIs (Key Performance Indicators)](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#kpis-key-performance-indicator-)
- [Dashboard Final](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#dashboard-final-siniestros-viales-)
- [Streamlit](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#streamlit-)
- [Conclusiones](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#conclusiones-)
- [Sugerencias](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#sugerencias-)

## Contexto 🌍

El Observatorio de Movilidad y Seguridad Vial de la Ciudad genera información fehaciente que nos permite tomar decisiones de manera conjunta con vecinos, vecinas y la sociedad civil para mejorar la seguridad vial y la forma en la que nos movemos todos los días. Es por eso que necesita a los mejores analsitas de datos para este proyecto!

## Estructura del Proyecto 🏗️

- **/SQL**: Carpeta que contiene scripts SQL, un video explicativo sobre la conexión MySQL con PowerBI y documentación importante.
- **/dashboard**: Carpeta que contiene:
  - PPT explicando brevemente el dashboard.
  - Plantilla de Power BI y PDF.
  - Video breve de uso de Python en Power BI.
- **/data**: Directorio que almacena los datasets originales utilizados para el dashboard.
- **/images**: Directorio que contiene imágenes utilizadas en este repositorio.
- **/streamlit_siniestros_viales**: Directorio que contiene los archivos necesarios para el deploy de la app en Streamlit.
- **EDA_siniestros viales CABA.ipynb**: Notebook ejecutado de análisis exploratorio de datos.
- **ETL_siniestros viales CABA.ipynb**: Notebook ejecutado de ETL.
- **LICENSE**: Archivo que contiene la licencia del repositorio.

## Desarrollo del Proyecto 🚀

El *Observatorio de Movilidad y Seguridad Vial (OMSV)*, centro de estudios que se encuentra bajo la órbita de la *Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires*, nos solicita la elaboración de un proyecto de análisis de datos, con el fin de generar información que le permita a las autoridades locales tomar medidas para disminuir la cantidad de víctimas fatales de los siniestros viales.

  • Para cumplir con la solicitud realizaremos un *EDA (Analisis exploratorio de los datos)*, solicitud de *OMSV* para poder entender cual es la situación que se atravesó en *CABA* a través de información recaudada
  
  • *ETL (Extraction, Tranform and Load)*, ya conociendo los datos vamos a extraerlos con herramientas de ciencia de datos para transformar los datos, de tal manera que aporten valor real y permita una toma de decisiones para disminuir el porcentaje de siniestros viales

## <center>EDA (Exploratory Data Analysis) 📈

  Se me ha solicitado presentar un entregable en *Jupyter Notebooks* sobre los datasets en referencia que provienen de la página de gobierno de *Buenos Aires*. En este link [EDA_siniestros_viales_CABA](https://github.com/EliasIchi/PI2_Henry/blob/main/EDA_siniestros%20viales%20CABA.ipynb) encontrarás el reporte.
A simple vista, se entiende que se le dio mayor importancia en recaudar datos sobre fatalidades que lesiones, ya que el dataset de homicidios es el que tiene mayor información en cuánto años, y además, el que cuenta con información más ordenada.
  Mientras que el dataset de lesionados tiene gran cantidad de celdas "Sin Datos", lo cuál da a entender, que la prioridad lógica es conocer dónde, cómo y cuándo suceden fatalidades.

## <center>ETL (Extract, Transform, Load) 🔄

  En resumen, el proceso completo incluye la extracción de datos desde la URL del gobierno de *Buenos Aires*, la transformación inicial en Python utilizando *Pandas* en el siguiente Jupyter Notebook: [ETL_siniestros_viales_CABA](https://github.com/EliasIchi/PI2_Henry/blob/main/ETL.ipynb), la carga en una base de datos *MySQL*, y luego la limpieza y refinamiento más exhaustivo utilizando *Power Query*. Este enfoque garantiza que los datos estén limpios, estructurados y listos para su análisis posterior.

[![insert_datos_database (1)](https://github.com/EliasIchi/PI2_Henry/assets/124707045/fc10df28-3649-4c54-93ee-3977470987cd)](https://drive.google.com/file/d/1b9VdPckKImrS7aYJgD8X67ejIRoFNBZ8/view) &nbsp;&nbsp;&nbsp;&nbsp; [![images (2)](https://github.com/EliasIchi/PI2_Henry/assets/124707045/3b895cb0-fb2d-4b1f-a6b1-e2ea6f7570fc)](https://drive.google.com/file/d/1VUEaOMOLCzEJvQXavX1aJWX6H58ClrXH/view)

## KPIs (Key Performance Indicators) 📈

1. **_Reducir en un 10% la tasa de homicidios en siniestros viales_** de los últimos seis meses, en *CABA*, en comparación con la tasa de homicidios en siniestros viales del semestre anterior.

2. **_Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, en CABA,_** respecto al año anterior.

3. **_Reducir en un 10% la cantidad de accidentes en cruces en el último año, en CABA,_** respecto al año anterior.

(![kpis](https://github.com/EliasIchi/PI2_Henry/assets/124707045/c7e81a83-fd3a-4c97-9789-2e7aae6d3358))]()

## Dashboard Final Siniestros Viales 📊

Para finalizar, aquí tienes el reporte, un dashboard en *Power BI*, dentro de éste encontrarás gráficos dinámicos e interactivos con información clara y sencilla para poder entender el comportamiento de siniestros viales en *CABA* durante el período 2016 a 2021. Además, podrás descargar el pbix o plantilla de *Power BI* desde el repo y replicarlo. Te invito a ver un [video](https://drive.google.com/file/d/1WSo63q-5plclTY53NZ6q8754q98trYP8/view) al hacer clic en la imagen.

[![Dashboard_final](https://github.com/EliasIchi/PI2_Henry/assets/124707045/184fafc4-7960-4efe-8e46-b6e495118007)](https://drive.google.com/file/d/1WSo63q-5plclTY53NZ6q8754q98trYP8/view)

## Streamlit 🚀

*Streamlit* es un framework open source para la creación de aplicaciones web interactivas y basadas en datos. Está diseñado para facilitar la creación de aplicaciones de machine learning, visualización de datos y paneles de control de manera rápida y sencilla. Te invito a ver mi app en el siguiente enlace: [App Siniestros Viales](https://siniestros-viales-stream.streamlit.app/)

Puedes ver el video del deploy haciendo clic en la imagen:

[![](https://github.com/EliasIchi/PI2_Henry/assets/124707045/d9b1a59b-2fc3-4adf-8745-7bd9eaea5961)](https://drive.google.com/file/d/107nAYMLCiHLa7IM9BA4M2EgYxE4SI4Ih/view)

## Conclusiones 📝

Gracias al análisis exhaustivo de los datos aportados por el gobierno de la ciudad, notamos que:
- El género con mayor cantidad de víctimas es el masculino.
- Los principales acusados del hecho son los autos, transportes públicos y vehículos de carga.
- Históricamente la mayor cantidad de víctimas son conductores en moto, peatones y conductores de auto.
- La mayor cantidad de las víctimas en moto son de género masculino.
- La mayor cantidad de hechos sucede en los cruces (es decir, en esquinas).
- El rango etario de las víctimas fatales es entre 16 y 30 años, el género más afectado es masculino y suelen ser conductores de motos.
- En la comuna 1 es donde históricamente suceden mayormente los siniestros viales con fatalidades, los barrios son: Constitución- Montserrat- Puerto Madero - Retiro - San Nicolás - San Telmo, en este caso el tipo de víctima más afectado es el peatón y en segundo lugar motos.
- El tipo de calle donde mayormente suceden los incidentes es en avenidas, por ejemplo, en el mapa si se ve por comuna 1 se ve en la Avenida 9 de Julio los casos en mención.
- Los hechos que históricamente terminan en fatalidad suelen ser en el horario de 7,6 y 5 am (principalmente) y en cuanto a los días de la semana no hay días con menos o mayor diferencia a nivel histórico que marque gran diferencia.
- Los días que históricamente terminan en siniestro vial con homicidios son entre 13 y 15 de cada mes y; a fin de mes entre 26 y 29 de cada mes.

## Sugerencias 🛠️

En base a estos datos, algunas sugerencias para reducir la incidencia de siniestros viales con resultado de homicidio podrían ser:
- Implementar programas de educación vial dirigidos a conductores de todos los vehículos, con especial énfasis en conductores de motocicletas.
- Mejorar la infraestructura vial en áreas de alto riesgo, como intersecciones y cruces, mediante la instalación de semáforos, señalización adecuada y diseño de calles más seguras.
- Reforzar la aplicación de la ley de tránsito, especialmente en lo que respecta a conductas imprudentes como el exceso de velocidad, el consumo de alcohol al conducir y el uso de dispositivos móviles mientras se conduce.
- Promover el uso de equipos de seguridad, como cascos para motociclistas y cinturones de seguridad para conductores y pasajeros de vehículos.

¡Gracias por visitar nuestro repositorio! Esperamos que este proyecto sea útil para comprender y abordar el problema de los siniestros viales en la Ciudad Autónoma de Buenos Aires. 🚦🛑
