from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, desc

# 1. Crear sesión de Spark
spark = SparkSession.builder \
    .appName("Smartphone_Addiction_Batch_Analysis") \
    .getOrCreate()

# 2. Cargar el conjunto de datos de Kaggle
# Asegúrate de que el nombre del archivo coincida con el descargado
df_addiction = spark.read.csv(
    "smartphone_addiction_data.csv", 
    header=True, 
    inferSchema=True
)

print("Datos iniciales:")
df_addiction.show(5)

# 3. Limpieza de datos (Drop NaNs) [cite: 35]
df_clean = df_addiction.dropna()

# 4. Análisis Exploratorio de Datos (EDA)
# Calculamos el promedio de uso diario por tipo de aplicación
usage_analysis = df_clean.groupBy("App_Opened") \
    .agg(avg("Daily_Usage_Hours").alias("Avg_Daily_Hours")) \
    .orderBy(desc("Avg_Daily_Hours"))

print("Análisis de uso promedio por aplicación:")
usage_analysis.show()

# 5. Filtrado de usuarios con uso crítico (ej. más de 6 horas)
critical_users = df_clean.filter(col("Daily_Usage_Hours") > 6) \
    .select("User_ID", "Age", "Daily_Usage_Hours", "App_Opened")

print("Usuarios con niveles de uso críticos detectedos:")
critical_users.show(10)

# 6. Detener la sesión
spark.stop()