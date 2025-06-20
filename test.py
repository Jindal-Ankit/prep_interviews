from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
spark.range(10).show()