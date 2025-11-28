# Definición de los datos

## Origen de los datos

La base de datos utilizada en este proyecto proviene de Kaggle y se obtuvo directamente del siguiente enlace:
https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction?resource=download

El archivo original (heart.csv) se encuentra almacenado en la carpeta data/.

## Especificación de los scripts para la carga de datos

Los scripts responsables de la ingesta y lectura de los datos están ubicados en la carpeta scripts/data_acquisition/.
Estos scripts realizan la carga inicial del archivo heart.csv y validan su estructura antes del procesamiento.

## Referencias a rutas o bases de datos origen y destino

El dataset de origen está ubicado en la ruta data/heart.csv.
Los datos procesados y analizados se referencian desde los notebooks y scripts contenidos en la carpeta eda/

### Rutas de origen de datos

La ubicación del archivo fuente corresponde a data/heart.csv.
La estructura de origen se mantiene igual a la entregada por Kaggle, con todas las variables originales.
Las transformaciones y verificaciones iniciales se documentan en los scripts de data_acquisition/ y el análisis exploratorio se registra en docs/data/data_summary.md.

### Base de datos de destino

En esta fase del proyecto aún no se ha iniciado el modelamiento; por tanto, no se han definido ni generado bases de datos de destino.
Actualmente, el trabajo se centra exclusivamente en la exploración, limpieza y descripción del dataset original mediante los notebooks de EDA.
