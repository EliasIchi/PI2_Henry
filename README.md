# <center>Siniestros Viales (CABA)<center>

Bienvenidos al repositorio de proyecto individual n°2 de la carrera ciencia de datos en Henry

![accidentes_viales](https://github.com/EliasIchi/PI2_Henry/assets/124707045/608f8a08-7bb6-408c-be8b-2480f43afab8)

## Data Analyst
En esta oportunidad Henry nos desafía a crear un proyecto desde el rol de analista de datos, para ello, se plantean ciertos requerimientos que serán recorridos en este repositorio

## Índice

- [Contexto](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#contexto)<br>
- [Estructura del proyecto](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#estructura-del-proyecto)<br>
- [Desarrollo del proyecto](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#desarrollo-del-proyecto)<br>
- [EDA (Exploratory Data Analysis)](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#eda-exploratory-data-analysis)<br>
- [ETL (Extract, Transform, Load)](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#etl-extract-transform-load)<br>
- [KPIs (key performance indicator)](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#kpis-key-performance-indicator)<br>
- [Dashboard final](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#dashboard-final-siniestros-viales)<br>
- [Streamlit](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#streamlit)<br>
- [Conclusiones](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#conclusiones)<br>
- [Sugerencias](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#sugerencias)<br>


## Contexto:
La Agencia Nacional de Seguridad Vial dio a conocer que durante el año 2021, 3.861 personas fallecieron como consecuencia de siniestros viales. La cifra representa una disminución del 21% de víctimas mortales con respecto al 2019, año comparable en términos de circulación prepandemia. Además, es la cifra más baja de siniestralidad vial desde 2008. Las estadísticas de la ANSV se realizan en conjunto con todas las provincias, son oficiales, contrastables y con posibilidad de identificación individual de las personas fallecidas.

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




## Desarrollo del Proyecto
El Observatorio de Movilidad y Seguridad Vial (OMSV), centro de estudios que se encuentra bajo la órbita de la Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires, nos solicita la elaboración de un proyecto de análisis de datos, con el fin de generar información que le permita a las autoridades locales tomar medidas para disminuir la cantidad de víctimas fatales de los siniestros viales.

  • Para cumplir con la solicitud realizaremos un EDA (Analisis exploratorio de los datos), solicitud de OMSV para poder entender cual es la situación que se atravesó en CABA a través de información recaudada
  
  • ETL (Extraction, Tranform and Load), ya conociendo los datos vamos a extraerlos con herramientas de ciencia de datos para transformar los datos, de tal manera que aporten valor real y permita una toma de decisiones para disminuir el porcentaje de siniestros viales

## <center>EDA (Exploratory Data Analysis)

  Se me ha solicitado presentar un entregable en jupyter notebooks sobre los datasets en referencia que provienen de la página de gobierno de Bs As.
  En este link <A HREF=https://github.com/EliasIchi/PI2_Henry/blob/main/EDA_siniestros%20viales%20CABA.ipynb>EDA_siniestros_viales_CABA</A> encontrarás el reporte.
A simple vista, se entiende que se le dió mayor importancia en recaudar datos sobre fatalidades que lesiones, ya que el dataset de homicidios es el que tiene mayor información en cuánto años, y además, el que cuenta con información más ordenada.
  Mientras que el dataset de lesionados tiene gran cantidad de celdas "Sin Datos", lo cuál da a entender, que la prioridad lógica es conocer donde, como y cuando suceden fatalidades.


## <center>ETL (Extract, Transform, Load)
  En resumen, el proceso completo incluye la extracción de datos desde la URL del gobierno de Buenos Aires, la transformación inicial en Python utilizando Pandas en el siguiente Jupyter Notebook: <A HREF=https://github.com/EliasIchi/PI2_Henry/blob/main/ETL.ipynb>ETL_siniestros_viales_CABA</A>, la carga en una base de datos MySQL, y luego la limpieza y refinamiento más exhaustivo utilizando Power Query. Este enfoque garantiza que los datos estén limpios, estructurados y listos para su análisis posterior.  


<A HREF=https://drive.google.com/file/d/1b9VdPckKImrS7aYJgD8X67ejIRoFNBZ8/view>![insert_datos_database (1)](https://github.com/EliasIchi/PI2_Henry/assets/124707045/fc10df28-3649-4c54-93ee-3977470987cd)</A> &nbsp;&nbsp;&nbsp;&nbsp; <A HREF=https://drive.google.com/file/d/1VUEaOMOLCzEJvQXavX1aJWX6H58ClrXH/view>![images (2)](https://github.com/EliasIchi/PI2_Henry/assets/124707045/3b895cb0-fb2d-4b1f-a6b1-e2ea6f7570fc)</A>


## <center>KPIs (key performance indicator)
1. **Reducir en un 10% la tasa de homicidios en siniestros viales** *de los últimos seis meses, en CABA,* **en comparación con la tasa de homicidios en siniestros viales del semestre anterior.**

    Definimos a la *tasa de homicidios en siniestros viales* como el número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes en un área geográfica durante un período de tiempo específico. Su fórmula es: **(Número de homicidios en siniestros viales / Población total) * 100,000**

2. **Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, en CABA,** **respecto al año anterior.**

    Definimos a la *cantidad de accidentes mortales de motociclistas en siniestros viales* como el número absoluto de accidentes fatales en los que estuvieron involucradas víctimas que viajaban en moto en un determinado periodo temporal. Su fórmula para medir la evolución de los accidentes mortales con víctimas en moto es: **(Número de accidentes mortales con víctimas en moto en el año anterior - Número de accidentes mortales con víctimas en moto en el año actual) / (Número de accidentes mortales con víctimas en moto en el año anterior) * 100**

3. **Reducir en un 10% la cantidad de accidentes en cruces en el último año, en CABA,** **respecto al año anterior.**

    Definimos a la *cantidad de accidentes mortales en cruces en siniestros viales* como el número absoluto de accidentes fatales en los que estuvieron involucradas víctimas en cruces en un determinado periodo temporal. Su fórmula para medir la evolución de los accidentes mortales en cruces es: **(Número de accidentes mortales con víctimas en cruces en el año anterior - Número de accidentes mortales con víctimas en cruces año actual) / (Número de accidentes mortales con víctimas en cruces en el año anterior) * 100**

   
![kpis (1)](https://github.com/EliasIchi/PI2_Henry/assets/124707045/400f359e-9609-4a7b-9c93-07699091b30a)


## <center>Dashboard Final Siniestros Viales
Para finalizar he aqui el reporte, un dashboard en power bi,
dentro de éste encontrarás gráficos dinámicos e iinteractivos con información clara y sencilla para poder entender el comportamiento de siniestros viales en CABA durante el período 2016 a 2021, no solo encontrarás gráficos, sino también conclusiones y datos interesantes para tomar decisiones a futuro.
 Ademas podrás descargar el pbix o plantilla de power bi desde el repo y replicarlo.
 Te invito a ver un video al hacer click en la imagen.
Que lo disfrutes!!!


<A HREF=https://drive.google.com/file/d/1WSo63q-5plclTY53NZ6q8754q98trYP8/view>![Dashboard_final](https://github.com/EliasIchi/PI2_Henry/assets/124707045/184fafc4-7960-4efe-8e46-b6e495118007)</A>

## Streamlit:
Streamlit es un framework open source para la creación de aplicaciones weqb interactivas y basadas en datos. Está diseñado para facilitar la creación de aplicaciones de machine learning, visualización de datos y paneles de control de manera rápida y sencilla.
  Te invito a ver mi app en el siguiente enlace: <A HREF=https://siniestros-viales-stream.streamlit.app/>[App Siniestros Viales]</A>

  Puede ver video del deploy en el siguiente enlace, haciendo click en la imagen:


<A HREF=https://drive.google.com/file/d/107nAYMLCiHLa7IM9BA4M2EgYxE4SI4Ih/view>![](https://github.com/EliasIchi/PI2_Henry/assets/124707045/d9b1a59b-2fc3-4adf-8745-7bd9eaea5961)</A>



## Conclusiones

Gracias al análisis exhaustivos de los datos aportados por el gobierno de la ciudad, notamos que:

1. El género con mayor cantidad de víctimas es el masculino.
2. Los principales acusados del hecho son los autos, transportes públicos y vehículos de carga.
3. Históricamente la mayor cantidad de víctimas son conductores en moto, peatones y conductores de auto.
4. La mayor cantidad de las víctimas en moto son de género masculino.
5. La mayor cantidad de hechos sucede en los cruces (es decir, en esquinas).
6. El rango etario de las víctimas fatales es entre 16 y 30 años, el género más afectado es masculino y suelen ser conductores de motos.
7. En la comuna 1 es donde históricamente suceden mayormente los siniestros viales con fatalidades, los barrios son: Constitución- Montserrat- Puerto Madero - Retiro - San Nicolás - San Telmo, en este caso el tipo de víctima más afectado es el peatón y en segundo lugar motos.
8. El tipo de calle donde mayormente suceden los incidentes es en avenidas, por ejemplo, en el mapa si se ve por comuna 1 se ve en la Avenida 9 de Julio los casos en mención.
9. Los hechos que históricamente terminan en fatalidad suelen ser en el horario de 7,6 y 5 am (principalmente) y en cuanto a los días de la semana no hay días con menos o mayor diferencia a nivel histórico que marque gran diferencia.
10. Los días que históricamente terminan en siniestro vial con homicidios son entre 13 y 15 de cada mes y; a fin de mes entre 26 y 29 de cada mes.

## Sugerencias

En base a estos datos, algunas sugerencias para reducir la incidencia de siniestros viales con resultado de homicidio podrían ser:

- Implementar programas de educación vial dirigidos a conductores de todos los vehículos, con especial énfasis en conductores de motocicletas.
- Mejorar la infraestructura vial en áreas de alto riesgo, como intersecciones y cruces, mediante la instalación de semáforos, señalización adecuada y diseño de calles más seguras.
- Reforzar la aplicación de la ley de tránsito, especialmente en lo que respecta a conductas imprudentes como el exceso de velocidad, el consumo de alcohol al conducir y el uso de dispositivos móviles mientras se conduce.
- Promover el uso de equipos de seguridad, como cascos para motociclistas y cinturones de seguridad para conductores y pasajeros de vehículos.
