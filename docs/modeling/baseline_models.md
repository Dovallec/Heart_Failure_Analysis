# Reporte del Modelo Baseline

Este documento detalla la implementación y los resultados del primer modelo predictivo, una Regresión Logística, que sirve como la línea base de rendimiento para el proyecto.

## Descripción del Modelo

El modelo seleccionado como **baseline** práctico y sensible para el proyecto es la **Regresión Logística**. Este algoritmo lineal es simple, altamente interpretable y rápido de entrenar, lo que lo estableció como el punto de partida para la clasificación binaria de la enfermedad cardíaca.

**Baseline Teórico (Referencia):**
La clase objetivo más frecuente es **1 (HeartDisease)**, con una proporción del **55.34%**. El modelo de Regresión Logística debe superar esta exactitud para ser considerado viable y útil.

## Variables de Entrada

El modelo fue entrenado utilizando **15 características** del conjunto de datos.

| Tipo de Variable | Variables Originales | Preprocesamiento en Baseline | Variables Resultantes (Total: 15) |
| :--- | :--- | :--- | :--- |
| **Numéricas** | `Age`, `RestingBP`, `Cholesterol`, `FastingBS`, `MaxHR`, `Oldpeak` | Escalado con `StandardScaler` (En iteración posterior a la carga de datos). | 6 variables |
| **Categóricas** | `Sex`, `ChestPainType`, `RestingECG`, `ExerciseAngina`, `ST_Slope` | Codificación One-Hot Encoding (`pd.get_dummies` con `drop_first=True`). | 9 variables dummy |

## Variable Objetivo

El modelo intenta predecir si un paciente tiene enfermedad cardíaca o no:

| Valor | Descripción |
| :--- | :--- |
| **0** | No hay enfermedad cardíaca |
| **1** | Sí hay enfermedad cardíaca |

La variable se encuentra aproximadamente balanceada (55.34% vs 44.66%).

## Evaluación del Modelo

### Métricas de Evaluación

Se utilizaron métricas de clasificación reportadas en el conjunto de prueba para establecer una visión completa del rendimiento:

| Métrica | Descripción |
| :--- | :--- |
| **Accuracy (Exactitud)** | Proporción de predicciones correctas totales. |
| **Precision (Precisión)** | Capacidad para evitar Falsos Positivos. |
| **Recall (Sensibilidad)** | Capacidad para evitar Falsos Negativos (crucial en contextos de salud). |
| **F1-Score** | Media armónica de Precision y Recall. |

### Resultados de Evaluación

Los resultados presentados a continuación corresponden a la primera implementación de la Regresión Logística:

| Clase | Precision | Recall | F1-Score | Soporte |
| :--- | :--- | :--- | :--- | :--- |
| **0 (No Enfermedad)** | 0.88 | 0.79 | 0.83 | 82 |
| **1 (Enfermedad)** | 0.85 | **0.91** | 0.88 | 102 |
| **Accuracy (Exactitud)** | \- | \- | \- | **0.86** |
| **Promedio Ponderado** | 0.86 | 0.86 | 0.86 | 184 |

## Análisis de los Resultados

**Fortalezas del Modelo Baseline:**
* **Alto Rendimiento Inicial:** Con una Exactitud del **86%**, el modelo supera ampliamente el *baseline* teórico (55.34%), confirmando que el conjunto de características tiene un fuerte poder predictivo.
* **Alta Sensibilidad Clínica (Recall):** El modelo destaca por su **alto Recall en la Clase 1 (0.91)**. En el contexto médico, esto indica una gran capacidad para **identificar correctamente a los pacientes enfermos**, minimizando el riesgo de **Falsos Negativos** (pacientes enfermos que son dados de alta incorrectamente), lo cual es una prioridad.

**Debilidades del Modelo Baseline:**
* **Baja Especificidad:** El **Recall en la Clase 0 (0.79)** es inferior. Esto sugiere que el modelo produce una cantidad significativa de **Falsos Positivos** (pacientes predichos como enfermos que en realidad no lo están). La optimización debe enfocarse en reducir estos Falsos Positivos para mejorar la Precisión general.
* **Sesgo Potencial:** La inclusión de los valores anómalos de `Cholesterol=0` en el entrenamiento podría estar afectando la robustez de los coeficientes del modelo.

## Conclusiones

La Regresión Logística establece un **sólido punto de partida** con un rendimiento general del 86%. Su principal ventaja es la alta sensibilidad para detectar la enfermedad, lo que lo convierte en un candidato fuerte para la fase de producción, sujeto a optimización.

**Posibles Áreas de Mejora (Próximos Sprints):**
1.  **Optimización de Hiperparámetros:** Aplicar `GridSearchCV` para mejorar el rendimiento, especialmente la Precisión.
2.  **Selección de Características:** Utilizar métodos univariantes (F-Score, Información Mutua) para validar y simplificar el conjunto de predictores, buscando un equilibrio óptimo entre complejidad y rendimiento.

## Referencias

* Modelo: `sklearn.linear_model.LogisticRegression`
* Evaluación: `sklearn.metrics.classification_report`, `sklearn.metrics.accuracy_score`
