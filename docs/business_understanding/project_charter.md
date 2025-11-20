# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Predicción de Eventos de Enfermedad Cardíaca

## Objetivo del Proyecto

Desarrollar un modelo de machine learning supervisado aplicando técnicas de metodologías ágiles  para predecir la presencia de enfermedad cardíaca (HeartDisease = 1) a partir de variables clínicas, demográficas y resultados electrocardiográficos.

El propósito es desarrollar un modelo robusto que permita identificar patrones de riesgo elevados, utilizando técnicas de aprendizaje de máquina sobre el conjunto de datos seleccionado aplicando técnicas de metodologías agiles que permitan un desarrollo eficiente del proyecto a lo largo de su ciclo de vida.

## Alcance del Proyecto

### Incluye:

- [Descripción de los datos disponibles]
  
El dataset contiene 12 variables relevantes en el diagnóstico de enfermedad cardíaca las cuales se enuncian a continuación:

    - Age: edad del paciente.
    - Sex: sexo (M/F).
    - Chest Pain Type: TA, ATA, NAP, ASY.
    - Resting BP: presión arterial en reposo (mmHg).
    - Cholesterol: colesterol sérico (mg/dl).
    - Fasting BS: azúcar en ayunas > 120 mg/dl (1: sí, 0: no).
    - Resting ECG: estado del electrocardiograma (Normal/ST/LVH).
    - Max HR: frecuencia cardíaca máxima alcanzada.
    - Exercise Angina: angina inducida por ejercicio (Y/N).
    - Oldpeak: depresión del ST medida durante ejercicio.
    - ST_Slope: pendiente del segmento ST (Up/Flat/Down).
    - HeartDisease: variable respuesta (1 = enfermedad cardíaca, 0 = normal).

- [Descripción de los resultados esperados]
  
En el desarrollo del proyecto se espera lograr un entendimiento profundo del conjunto de datos, garantizando la correcta aplicación de técnicas de limpieza, transformación y preprocesamiento que permitan preparar las variables para el modelado supervisado. Este proceso incluye la identificación de patrones, distribución de las variables, análisis de correlaciones y tratamiento de valores atípicos o inconsistencias, con el fin de establecer una base analítica sólida para el entrenamiento de los modelos.

Asimismo, se anticipa la construcción y evaluación de diferentes modelos de clasificación supervisada, comparando su desempeño mediante métricas estándar como precisión, recall, F1-score, matriz de confusión y medidas basadas en curvas de discriminación. Finalmente, se espera realizar un análisis integral de los resultados para justificar la selección del modelo óptimo, considerando tanto su rendimiento cuantitativo como su comportamiento interpretativo y capacidad de generalización.

- [Criterios de éxito del proyecto]
  
El proyecto se considerará exitoso si el modelo supervisado demuestra un desempeño sólido y estable, evidenciando capacidad para diferenciar de forma consistente entre pacientes con y sin enfermedad cardíaca y manteniendo un adecuado equilibrio entre precisión y generalización. Además, el pipeline de preprocesamiento, entrenamiento y validación debe ser completamente reproducible, estar documentado con rigurosidad técnica y permitir interpretar claramente los factores que influyen en las predicciones mediante técnicas explicativas apropiadas. El trabajo deberá desarrollarse aplicando principios de metodologías ágiles de gestión de proyectos, garantizando iteración continua, retroalimentación frecuente y una entrega incremental que asegure el avance ordenado y eficiente del desarrollo analítico.

### Excluye:

- [Descripción de lo que no está incluido en el proyecto]

El proyecto no incluye actividades relacionadas con el despliegue del modelo en entornos clínicos o productivos, la integración con sistemas hospitalarios, ni la recolección adicional de datos fuera del dataset proporcionado. Tampoco contempla la generación de recomendaciones médicas, diagnósticos clínicos o decisiones terapéuticas. De igual forma, quedan fuera del alcance la construcción de interfaces visuales, aplicaciones web, dashboards o herramientas de visualización avanzada, y cualquier procesamiento de datos no estructurados o provenientes de nuevas fuentes externas.

## Metodología

La metodología del proyecto seguirá un enfoque basado en CRISP-DM. En la primera etapa, se realizará un Análisis Exploratorio de Datos (EDA) sobre el conjunto de datos, para entender sus características, distribuciones, y la presencia de datos atípicos o faltantes. Se aplicarán técnicas de limpieza, imputación, y en caso de ser necesario, codificación de variables categóricas (ej. One-Hot Encoding), o escalado de características numéricas, con el objetivo de preparar los datos para el entrenamiento. En la fase de modelado, se explorarán modelos de clasificación supervisada y se evaluará si es pertinente el diseño de arquitecturas de redes neuronales profundas, experimentando con el número de capas, la cantidad de neuronas por capa, las funciones de activación y las técnicas de regularización. Posteriormente, el conjunto de datos se dividirá en subconjuntos de entrenamiento, validación y prueba para garantizar una evaluación objetiva. Se entrenarán los modelos candidatos y se optimizarán sus hiperparámetros utilizando el conjunto de validación. Se realizará la evaluación y comparación de modelos utilizando métricas de clasificación estándar sobre un conjunto de prueba independiente, para validar su precisión y capacidad de generalización antes de presentar las conclusiones y los posibles pasos futuros. Finalmente, se espera que el modelo quede listo para ser desplegado por medio de un servicio web.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semana | del 13 de noviembre al 20 de noviembre |
| Preprocesamiento, análisis exploratorio | 1 semana | del 21 de noviembre al 27 de noviembre |
| Modelamiento | 1 semana | del 28 de noviembre al 4 de diciembre |
| Despliegue | 1 semana | del 5 de diciembre al 11 de diciembre |
| Evaluación y entrega final | 3 días | del 12 de diciembre al 13 de diciembre |

## Equipo del Proyecto

- Líder: David Santiago Ovalle Caviedes
- Ingeniero de datos: Juan Manuel Escobar Quinatana
- Científico de datos: David Santiago Ovalle Caviedes
- Ingeniera en ML: Ivonne Cristina Ruiz Páez

## Presupuesto

| Categoría de Gasto | Descripción | Costo Estimado (USD) | Notas / Consideraciones |
| :----------------- | :---------- | :------------------- | :---------------------- |
| **I. Personal** | | | |
| Científico de Datos Senior | Diseño del modelo, preprocesamiento avanzado, optimización. | $8,000 | 2 meses a tiempo parcial |
| Ingeniero de ML Junior | Implementación de código, experimentos, EDA. | $5,000 | 2.5 meses a tiempo completo |
| **II. Infraestructura y Software** | | | |
| Plataforma Cloud (GPU) | AWS/GCP/Azure para entrenamiento de modelos (instancias GPU). | $1,500 | Costos de cómputo por ~200 horas de GPU |
| Almacenamiento Cloud | S3/GCS para dataset de imágenes y checkpoints del modelo. | $50 | 500 GB por 2 meses |
| Licencias de Software | Herramientas específicas o IDEs (si aplica, asumimos open-source). | $0 | Se utilizarán herramientas y librerías open-source (Python, TensorFlow/PyTorch, scikit-learn). |
| **IV. Misceláneos** | | | |
| Investigación y Desarrollo | Tiempo para pruebas de concepto, lectura de artículos, etc. | $700 | Horas dedicadas a exploración y resolución de problemas. |
| Gestión de Proyecto | Coordinación, reuniones, documentación. | $300 | Pequeño porcentaje del tiempo del equipo. |
| Contingencias | Fondo para imprevistos (aprox. 10% del total). | $1,555 | Buffer para gastos inesperados. |
| **TOTAL ESTIMADO DEL PROYECTO** | | **$17,105** | |

## Stakeholders

- Los stakeholders clave en este proyecto son los médicos cardiólogos, y los analistas de datos en el sector salud, interesados en herramientas de apoyo para la identificación temprana de pacientes con riesgo elevado de enfermedad cardíaca.

- Los expertos en cardiología tienen un papel importante para actuar como validadores del conocimiento de dominio, asesorando sobre la pertinencia de las variables clínicas y la correcta interpretación de los resultados del modelo para asegurar su relevancia y utilidad clínica.

- Las expectativas giran en torno a la entrega de un modelo de machine learning que demuestre una alta capacidad predictiva y de discriminación (medida con métricas como la curva ROC y el F1-score) y que sea interpretable para identificar los factores de riesgo más influyentes en la predicción de la enfermedad cardíaca.

## Aprobaciones

- Juan Sebastian Malagón Torres (Líder del equipo de Ciencia de datos)
- [Firma del aprobador]
- [13 de Diciembre 2025]
