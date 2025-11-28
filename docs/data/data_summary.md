# Reporte de Datos

Este reporte presenta el análisis exploratorio de datos realizado sobre el dataset de predicción de falla cardíaca. Se incluyen la caracterización general, la calidad de los datos, el comportamiento de la variable objetivo, el análisis detallado de las variables, el ranking de importancia y la relación entre variables explicativas y la variable objetivo.

Para obtener la información que se presenta en este reporte, se elaboró un notebook de python (EDA_report_summary.ipynb) que se encuentra en la sección de: scripts/eda/EDA_report_summary.ipynb

## Resumen general de los datos

El dataset contiene 918 observaciones y 12 variables. Incluye variables numéricas como Age, RestingBP, Cholesterol, FastingBS, MaxHR y Oldpeak, además de variables categóricas como Sex, ChestPainType, RestingECG, ExerciseAngina y ST_Slope. Las estadísticas descriptivas indican que la edad promedio es 53.5 años, la presión arterial en reposo tiene un promedio de 132 mmHg con algunos valores atípicos igual a 0, el colesterol presenta una dispersión amplia entre 0 y 603 mg/dL, y la frecuencia cardíaca máxima se distribuye alrededor de 136 bpm. La variable objetivo HeartDisease contiene 508 casos positivos y 410 negativos, lo cual refleja una distribución razonablemente balanceada.

## Resumen de calidad de los datos

No existen valores faltantes en ninguna variable del dataset y no se encontraron filas duplicadas. El análisis de valores extremos utilizando el rango intercuartílico evidencia presencia significativa de outliers, especialmente en Cholesterol, RestingBP y Oldpeak. En el caso de FastingBS, el método IQR lo clasifica como extremo debido a su naturaleza binaria. Los boxplots muestran alta variabilidad en Cholesterol y Oldpeak, lo cual deberá tenerse en cuenta en fases posteriores del modelado.

## Variable objetivo

La variable HeartDisease muestra una distribución del 55% para la clase positiva y 45% para la negativa. Esta ligera asimetría no representa un problema significativo para tareas de clasificación, ya que el dataset mantiene un nivel adecuado de balance. La distribución gráfica confirma la predominancia moderada de la clase positiva.

## Variables individuales

Las variables numéricas muestran patrones relevantes: Age presenta una distribución cercana a la normal y los pacientes con enfermedad tienden a ser mayores. RestingBP presenta asimetría y ciertos valores anómalos. Cholesterol tiene una distribución muy dispersa con una cola bastante larga hacia valores altos. MaxHR se distribuye alrededor de 136 bpm y es notablemente menor en pacientes con enfermedad. Oldpeak está sesgada hacia valores bajos, pero aumenta significativamente en la clase positiva.

Las variables categóricas también presentan comportamientos diferenciados: el sexo masculino (Sex = M) aparece más frecuentemente en la clase positiva. El tipo de dolor en el pecho ChestPainType = ASY está fuertemente asociado con la presencia de enfermedad. La variable ExerciseAngina = Y aparece con mayor frecuencia en pacientes con diagnóstico positivo. Finalmente, la pendiente del segmento ST ST_Slope = Flat es más común en la clase positiva.

## Ranking de variables

El análisis indica que las variables con mayor capacidad predictiva frente a la variable objetivo son Oldpeak, MaxHR y Age, junto con las categóricas ChestPainType (especialmente la categoría ASY), ExerciseAngina y ST_Slope (particularmente la categoría Flat). Estas variables muestran clara separación entre las clases tanto en las distribuciones como en los boxplots y constituyen los predictores más influyentes según el análisis exploratorio.

## Relación entre variables explicativas y variable objetivo

La relación entre las variables explicativas y HeartDisease confirma patrones clínicamente consistentes. Los pacientes de la clase positiva tienden a ser mayores, presentan valores menores de MaxHR y mayores valores de Oldpeak. En el plano categórico, los pacientes con enfermedad se concentran en ChestPainType = ASY, ExerciseAngina = Y y ST_Slope = Flat. En contraste, variables como Cholesterol y RestingBP, aunque presentan valores extremos, no muestran una separación marcada entre clases.
