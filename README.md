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
- [Dashboard_final](https://github.com/EliasIchi/PI2_Henry/blob/main/README.md#dashboard-final-siniestros-viales)<br>

## Contexto:
La Agencia Nacional de Seguridad Vial dio a conocer que durante el año 2021, 3.861 personas fallecieron como consecuencia de siniestros viales. La cifra representa una disminución del 21% de víctimas mortales con respecto al 2019, año comparable en términos de circulación prepandemia. Además, es la cifra más baja de siniestralidad vial desde 2008. Las estadísticas de la ANSV se realizan en conjunto con todas las provincias, son oficiales, contrastables y con posibilidad de identificación individual de las personas fallecidas.

## Estructura del Proyecto

• /SQL  > Carpeta que contiene scripts SQL, un video explicativo sobre la conexión MySQL con PowerBI y documentación importante.

• /data  > Directorio que almacena los datasets originales utilizados para el dashboard.

• /images  > Directorio que contiene imágenes utilizadas en este repositorio.

• EDA_siniestros viales CABA.ipynb  > Script Python para análisis exploratorio de datos.

• LICENSE  > Archivo que contiene la licencia del repositorio.

• README.md  > Archivo README del proyecto.

## Desarrollo del Proyecto
El Observatorio de Movilidad y Seguridad Vial (OMSV), centro de estudios que se encuentra bajo la órbita de la Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires, nos solicita la elaboración de un proyecto de análisis de datos, con el fin de generar información que le permita a las autoridades locales tomar medidas para disminuir la cantidad de víctimas fatales de los siniestros viales.

  • Para cumplir con la solicitud realizaremos un EDA (Analisis exploratorio de los datos), solicitud de OMSV para poder entender cual es la situación que se atravesó en CABA a través de información recaudada
  
  • ETL (Extraction, Tranform and Load), ya conociendo los datos vamos a extraerlos con herramientas de ciencia de datos para transformar los datos, de tal manera que aporten valor real y permita una toma de decisiones para disminuir el porcentaje de siniestros viales

## <center>EDA (Exploratory Data Analysis)

  Se me ha solicitado presentar un entregable en jupyter notebooks sobre los datasets en referencia que provienen de la página de gobierno de Bs As.
  En este link <A HREF=https://github.com/EliasIchi/PI2_Henry/blob/main/EDA_siniestros%20viales%20CABA.ipynb>EDA_siniestros_viales_CABA</A> encontrarás el reporte.
A simple vista, se entiende que se le dió mayor importancia en recaudar datos sobre fatalidades que lesiones, ya que el dataset de homicidios es el que tiene mayor información en cuánto años, y además, el que cuenta con información más ordenada.
  Mientras que el dataset de lesionados tiene gran cantidad de celdas "Sin Datos", lo cuál da a entender, que la prioridad lógica es conocer donde, como y cuando suceden fatalidades.


  

#### Datos más relevantes:
  1) La cantidad más normal de víctimas por siniestros viales con homicidios es de 1 persona por hecho.
  2) La mayor cantidad de victimas suelen estar en moto, le siguen los peatones y en tercer lugar autos.
  3) Los principales acusados del siniestro suelen ser autos, en segundo lugar con transportes públicos con pasajeros y en tercer lugar vehiculos de carga.
  4) El sexo de las víctimas fatales es mayor en masculino por gran diferencia al femenino.
  5) La comuna que tiene mayor cantidad de fatalidades es en la Comuna 1
  6) El año con mayor cantidad de fatalidades por siniestros viales fue 2018 y el menor 2020 (año pandemia COVID, con protocolo #Quedateencasa.
  7) Las mayor cantidad de victimas que terminaron en fatalidad entran en grupos de 16 - 30 años.
  8) Los horarios donde se visualizan mayor cantidad de siniestros viales es 6, 7 y 9 am

## <center>ETL (Extract, Transform, Load)
  En resumen, el proceso completo incluye la extracción de datos desde la URL del gobierno de Buenos Aires, la transformación inicial en Python utilizando Pandas en el siguiente Jupyter Notebook: <A HREF=https://github.com/EliasIchi/PI2_Henry/blob/main/ETL.ipynb>ETL_siniestros_viales_CABA</A>, la carga en una base de datos MySQL, y luego la limpieza y refinamiento más exhaustivo utilizando Power Query. Este enfoque garantiza que los datos estén limpios, estructurados y listos para su análisis posterior.  


<A HREF=https://drive.google.com/file/d/1b9VdPckKImrS7aYJgD8X67ejIRoFNBZ8/view>![insert_datos_database (1)](https://github.com/EliasIchi/PI2_Henry/assets/124707045/fc10df28-3649-4c54-93ee-3977470987cd)</A> &nbsp;&nbsp;&nbsp;&nbsp; <A HREF=https://drive.google.com/file/d/1VUEaOMOLCzEJvQXavX1aJWX6H58ClrXH/view>![images (2)](https://github.com/EliasIchi/PI2_Henry/assets/124707045/3b895cb0-fb2d-4b1f-a6b1-e2ea6f7570fc)</A>


## <center>Dashboard Final Siniestros Viales
Para finalizar he aqui el reporte, un dashboard en power bi,
dentro de este reporte encontrarás gráficos dinámicos e iinteractivos con información clara y sencilla para poder entender el comportamiento de siniestros viales en CABA durante el período 2016 a 2021, no solo encontrarás gráficos, sino también conclusiones y datos interesantes para tomar decisiones a futuro.
 Ademas podrás descargar el pbix o plantilla de power bi desde el repo y replicarlo.
 Te invito a ver un video al hacer click en la imagen.
Que lo disfrutes!!!


<A HREF=https://drive.google.com/file/d/1WSo63q-5plclTY53NZ6q8754q98trYP8/view>![Dashboard_final](https://github.com/EliasIchi/PI2_Henry/assets/124707045/184fafc4-7960-4efe-8e46-b6e495118007)</A>
