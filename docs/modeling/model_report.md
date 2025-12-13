# Reporte del Modelo Final

## Resumen Ejecutivo

El proyecto **Predicción de Eventos de Enfermedad Cardíaca** ha concluido con el desarrollo y despliegue de un modelo de **Regresión Logística** optimizado. El modelo fue seleccionado por su capacidad de ofrecer un alto rendimiento predictivo combinado con una interpretabilidad clínica significativa, un requisito fundamental en el ámbito de la salud.

El modelo alcanzó una **Precisión (Accuracy) del 89.13%** sobre el conjunto de prueba, con un balance adecuado entre la predicción de casos positivos (Recall 0.93) y negativos (Precision 0.91). El modelo fue registrado y desplegado exitosamente utilizando la plataforma **MLflow**, garantizando la trazabilidad y la disponibilidad como un servicio web de inferencia.

| Métrica | Clase 0 (Sin Enfermedad) | Clase 1 (Con Enfermedad) | Macro Promedio |
| :--- | :--- | :--- | :--- |
| **Precision** | 0.91 | 0.88 | 0.89 |
| **Recall** | 0.84 | 0.93 | 0.89 |
| **F1-Score** | 0.87 | 0.90 | 0.89 |
| **Accuracy Total** | \- | \- | 0.89 |

## Descripción del problema

El problema central es la clasificación binaria de pacientes para predecir la presencia o ausencia de enfermedad cardíaca (`HeartDisease = 1` o `0`).

**Contexto y Objetivos:**
* **Contexto:** El proyecto se desarrolla en el marco de la aplicación de metodologías ágiles a proyectos de Machine Learning, utilizando el conjunto de datos de predicción de falla cardíaca de Kaggle.
* **Objetivo:** Desarrollar un modelo predictivo supervisado robusto que permita identificar patrones de riesgo elevados para la enfermedad cardíaca a partir de 12 variables clínicas y demográficas.
* **Justificación:** El modelo ofrece una herramienta no invasiva y automatizada para la evaluación del riesgo, complementando la labor clínica.

## Descripción del modelo

El desarrollo siguió un enfoque híbrido, combinando las fases de **CRISP-DM** (Entendimiento, Preparación, Modelado, Evaluación) con la **iteración y feedback** constante de metodologías ágiles. 

### Modelo final seleccionado
El modelo final seleccionado fue la **Regresión Logística**, optimizado mediante `GridSearchCV`.

* **Modelo:** Regresión Logística.
* **Hiperparámetros Óptimos:**
    | Parámetro | Valor |
    | :--- | :--- |
    | `C` | 1.0 |
    | `penalty` | 'l2' |
    | `solver` | 'lbfgs' |
    | `class_weight` | 'balanced' |

### Técnicas y Metodología
1.  **Preparación de datos:** Codificación de variables categóricas (`Sex`, `ChestPainType`, `ST_Slope`, etc.) mediante **One-Hot Encoding** para transformarlas en formato numérico.
2.  **Selección de características:** Se utilizaron métodos univariantes como **ANOVA F-test** e **Información Mutua** (MI) para validar la relevancia de los predictores, lo que confirmó que `ST_Slope`, `Oldpeak`, y `MaxHR` son las características más influyentes. 
3.  **Modelado y optimización:** Se exploraron modelos *baseline* (Regresión Logística, Random Forest), y posteriormente se optimizaron los candidatos más prometedores (XGBoost y Regresión Logística) utilizando **GridSearchCV** para encontrar los mejores hiperparámetros.
4.  **MLOps y Despliegue:** El modelo fue registrado a través de **MLflow**, estableciendo un *pipeline* de despliegue estable.

## Evaluación del modelo

La evaluación se realizó sobre un conjunto de prueba (20% del total, 184 registros) retenido desde el inicio para garantizar la objetividad.

### Matriz de Confusión (Regresión Logística)

| Real / Predicho | No Enfermedad (0) | Con Enfermedad (1) |
| :--- | :--- | :--- |
| **No Enfermedad (0)** | 69 (Verdaderos Negativos) | 13 (Falsos Positivos) |
| **Con Enfermedad (1)** | 7 (Falsos Negativos) | 95 (Verdaderos Positivos) |

### Interpretación de los resultados

* **Alta Precisión (0.89):** El modelo tiene una alta capacidad para clasificar correctamente los casos.
* **Alto Recall en Clase Positiva (0.93):** De todos los pacientes que *realmente* tienen la enfermedad (102), el modelo identificó correctamente al 93% (95 casos). Esto es crucial en salud para minimizar los **Falsos Negativos** (casos de enfermedad perdidos).
* **F1-Score Balanceado (0.89):** El F1-score es alto para ambas clases, lo que indica que el modelo mantiene un buen balance entre Precision y Recall.

La evaluación muestra que la Regresión Logística optimizada es un modelo **robusto y confiable** para la predicción, con un desempeño comparable al de modelos más complejos (como XGBoost), pero ofreciendo mayor interpretabilidad.

## Conclusiones y Recomendaciones

### Ventajas del modelo
* **Interpretabilidad:** El uso de Regresión Logística permite una comprensión directa del impacto (coeficientes) de cada variable en la probabilidad de enfermedad.
* **Desempeño:** El Accuracy, Precision y Recall macro (0.89) cumplen con los criterios de solidez.
* **Reproducibilidad y despliegue:** El *pipeline* es completamente reproducible y el modelo fue exitosamente desplegado como un servicio REST API funcional utilizando MLflow.

### Limitaciones y Recomendaciones
* **Calidad de Datos:** **El proyecto no incluyó la limpieza de los 172 valores 0 en la variable `Cholesterol`**. Se recomienda imputación de estos valores anómalos (con la mediana o algún otro método) para validar si el rendimiento actual no está sesgado por este error de codificación.
* **Aplicación:** El modelo está listo para ser integrado en un sistema de información para el *screening* de riesgo (aplicación de pruebas o exámenes a una población aparentemente sana con el objetivo de detectar de forma temprana una enfermedad o condición específica antes de que aparezcan los síntomas.).

### Aplicaciones
El modelo, desplegado a través de su endpoint MLflow (`http://localhost:8001/invocations`), puede ser consumido por:
1.  **Dashboards de riesgo:** Para visualizar en tiempo real el riesgo de un paciente en función de sus parámetros de entrada.
2.  **Sistemas de admisión hospitalaria:** Como una alerta temprana automatizada para priorizar la atención o la realización de pruebas diagnósticas.

## Referencias

* Conjunto de datos: [Kaggle - Heart Failure Prediction](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction).
* Librerías de ML: `scikit-learn`, `xgboost`.
* MLOps: `mlflow` (para tracking, model registry y serving).
* Código fuente del proyecto: Repositorio GitHub de Heart\_Failure\_Analysis.
