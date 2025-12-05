# Reporte del Modelo Baseline: Regresión Logística

Este documento detalla la implementación y los resultados del primer modelo predictivo, una Regresión Logística, que sirve como la línea base de rendimiento para el proyecto.

## Descripción del modelo

El modelo seleccionado como *baseline* práctico es una **Regresión Logística**. Este algoritmo lineal es simple, interpretable y rápido de entrenar, lo que lo convierte en un excelente punto de partida para problemas de clasificación binaria.

* **Baseline Teórico (Referencia):**
    * La clase objetivo más frecuente es **1 (HeartDisease)**, con una proporción del **55.34%**. El modelo de Regresión Logística debe superar esta exactitud para ser considerado viable.

## Variables de entrada

El modelo fue entrenado utilizando **15 características** del conjunto de datos, luego de la ingeniería y codificación *one-hot* de las variables categóricas, sin aplicar selección de características en esta fase:

* **Variables Numéricas:** `Age`, `RestingBP`, `Cholesterol`, `FastingBS`, `MaxHR`, `Oldpeak`.
* **Variables Categóricas Codificadas:** `Sex_M`, `ChestPainType_ATA`, `ChestPainType_NAP`, `ChestPainType_TA`, `RestingECG_Normal`, `RestingECG_ST`, `ExerciseAngina_Y`, `ST_Slope_Flat`, `ST_Slope_Up`.

## Variable objetivo

El modelo intenta predecir si un paciente tiene enfermedad cardíaca o no:

| Valor | Descripción |
| :---: | :--- |
| `0` | No hay enfermedad cardíaca |
| `1` | Sí hay enfermedad cardíaca |

***

## Evaluación del modelo

### Métricas de evaluación

Se utilizaron las siguientes métricas de clasificación binaria, reportadas en el conjunto de prueba (`Test Set`):

| Métrica | Descripción |
| :--- | :--- |
| **Accuracy (Exactitud)** | Proporción de predicciones correctas totales. |
| **Precision (Precisión)** | De todos los casos predichos como positivos (1), cuántos fueron realmente positivos. Minimiza **Falsos Positivos**. |
| **Recall (Sensibilidad)** | De todos los casos positivos (1) reales, cuántos fueron predichos correctamente. Minimiza **Falsos Negativos**. |
| **F1-Score** | Media armónica de Precision y Recall. |

### Resultados de evaluación

A continuación, se presentan los resultados obtenidos por la Regresión Logística, optimizada mediante `GridSearchCV` en el conjunto de validación:

| Clase | Precision | Recall | F1-Score | Soporte |
| :---: | :---: | :---: | :---: | :---: |
| **0** (No Enfermedad) | 0.88 | 0.79 | 0.83 | 82 |
| **1** (Enfermedad) | 0.85 | 0.91 | 0.88 | 102 |
| **Accuracy (Exactitud)** | | | **0.86** | 184 |
| **Promedio Ponderado** | 0.86 | 0.86 | 0.86 | 184 |

### Análisis de los resultados

El modelo de Regresión Logística alcanzó una **Exactitud del 86%**, superando ampliamente el *baseline* teórico (55.34%), lo que confirma el poder predictivo de las características seleccionadas.

* **Fortaleza:** El modelo destaca por su **alto Recall en la Clase 1 (0.91)**. Esto es muy positivo en un contexto médico, ya que indica una gran capacidad para **identificar correctamente** a los pacientes enfermos, minimizando el riesgo de **Falsos Negativos**.
* **Debilidad:** El **Recall en la Clase 0 (0.79)** es inferior. Esto sugiere que el modelo produce más **Falsos Positivos** (pacientes predichos como enfermos que en realidad no lo están). La optimización en modelos posteriores debería enfocarse en mejorar la **Precisión** de la Clase 1 para reducir estos Falsos Positivos.

## Conclusiones

La Regresión Logística establece un **sólido punto de partida** con un rendimiento general del 86%. Su principal ventaja es la alta sensibilidad para detectar la enfermedad (Recall=0.91), priorizando la minimización de Falsos Negativos.

**Posibles Áreas de Mejora:**

1.  **Reducir Falsos Positivos:** Los modelos más complejos (como SVC y XGBoost) deben intentar mejorar la **Precisión** de la Clase 1 y el **F1-Score** de la Clase 0.
2.  **Impacto de la Selección de Características:** Se recomienda re-entrenar la Regresión Logística utilizando el subconjunto óptimo de 8 características identificado en las secciones posteriores del *notebook*, para verificar si un modelo más simple puede obtener un rendimiento similar o mejor.

## Referencias

1.  **Modelo:** `sklearn.linear_model.LogisticRegression`
2.  **Optimización:** `sklearn.model_selection.GridSearchCV`
3.  **Evaluación:** `sklearn.metrics.classification_report`, `sklearn.metrics.accuracy_score`
4.  **Datos:** Conjunto de datos de Heart Disease (`heart.csv`) cargado desde GitHub.
