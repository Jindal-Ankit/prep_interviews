import os

from pyspark.sql import SparkSession


def important_directories():
    root_dir_for_spark_sql = os.path.join(os.getcwd(), os.pardir, "metadata")
    #for DeltaCatalog
    metastore_dir = os.path.join(root_dir_for_spark_sql, 'metastore')
    spark_warehouse_dir = os.path.join(root_dir_for_spark_sql, 'spark_warehouse')

    print(f"creating metastore directory: {metastore_dir}")
    os.makedirs(metastore_dir, exist_ok=True)
    os.makedirs(spark_warehouse_dir, exist_ok=True)
    os.putenv("metastore_dir", metastore_dir)
    os.putenv("spark_warehouse_dir", spark_warehouse_dir)



def sparksession_with_delta_lake():
    """
        Initialize SparkSession with Delta Lake support
        The `configure_spark_with_delta_pip` function is a convenient way to add Delta Lake packages
        If you've set PYSPARK_SUBMIT_ARGS correctly, you might not strictly need this,
        but it's good practice.
    """
    important_directories()

    from delta.pip_utils import configure_spark_with_delta_pip
    metastore_warehouse_dir = os.getenv("metastore_warehouse_dir")
    spark_warehouse_dir = os.getenv("spark_warehouse_dir")
    builder = (
        SparkSession.builder.appName("DeltaLakeSetup")
        .master("local[*]")  # Use all available cores on your local machine
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .config("spark.hadoop.javax.jdo.option.ConnectionURL", f"jdbc:derby:;databaseName={metastore_warehouse_dir};create=true")
        .config("spark.hadoop.javax.jdo.option.ConnectionDriverName", "org.apache.derby.jdbc.EmbeddedDriver")
        .config("spark.hadoop.hive.metastore.warehouse.dir", spark_warehouse_dir)
        .config("spark.sql.warehouse.dir", spark_warehouse_dir)
        .config("spark.driver.extraJavaOptions", "-Dderby.system.home=" + metastore_warehouse_dir)
    )

    spark = configure_spark_with_delta_pip(builder).getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")  # Reduce verbose logging
    print("SparkSession created successfully with Delta Lake support!")
    return spark


class DeltaLakeSparkUtils:
    def __init__(self):
        pass


