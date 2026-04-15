# An-lisis-Spark
Procesamiento de Datos con Apache Spark y Kafka 🚀
Este proyecto desarrolla una infraestructura tecnológica para el análisis de grandes volúmenes de datos enfocada en la detección de patrones de adicción al smartphone. Se implementan soluciones de procesamiento tanto en lotes (batch) como en tiempo real (streaming).

📊 Dataset Utilizado
Nombre: Smartphone Addiction Prediction Data.
Descripción: Contiene registros de comportamiento de usuarios, incluyendo tiempo de uso diario, aplicaciones abiertas y conteo de notificaciones.

🛠️ Tecnologías EmpleadasApache Spark: 
Procesamiento distribuido de datos mediante RDDs y DataFrames.
Apache Kafka: Gestión de flujos de datos en tiempo real (Brokers, Topics, Producers/Consumers).
Python (PySpark): Lenguaje de programación para la implementación de la lógica de análisis.

📁 Estructura del Proyecto
batch_processing.py: Script de Spark para la limpieza, transformación y análisis exploratorio (EDA) de los datos históricos.
streaming_processing.py: (Próximamente) Implementación de Spark Streaming para consumir eventos desde Kafka.
data/: Directorio para el conjunto de datos seleccionado.

🚀 Instrucciones de Ejecución
Clonar el repositorio.
Asegurarse de tener instalado PySpark.
Ejecutar el script de análisis batch:

Bashpython batch_processing.py
