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

[Descripción breve de la metodología que se utilizará para llevar a cabo el proyecto]

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 2 semanas | del 1 de mayo al 15 de mayo |
| Preprocesamiento, análisis exploratorio | 4 semanas | del 16 de mayo al 15 de junio |
| Modelamiento y extracción de características | 4 semanas | del 16 de junio al 15 de julio |
| Despliegue | 2 semanas | del 16 de julio al 31 de julio |
| Evaluación y entrega final | 3 semanas | del 1 de agosto al 21 de agosto |

Hay que tener en cuenta que estas fechas son de ejemplo, estas deben ajustarse de acuerdo al proyecto.

## Equipo del Proyecto

- [Nombre y cargo del líder del proyecto]
- [Nombre y cargo de los miembros del equipo]

## Presupuesto

[Descripción del presupuesto asignado al proyecto]

## Stakeholders

- [Nombre y cargo de los stakeholders del proyecto]
- [Descripción de la relación con los stakeholders]
- [Expectativas de los stakeholders]

## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]
