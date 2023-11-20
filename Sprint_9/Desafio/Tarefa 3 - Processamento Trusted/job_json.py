import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from awsglue.transforms import ApplyMapping, SelectFields, ResolveChoice
from awsglue.utils import getResolvedOptions
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, IntegerType, DoubleType
from pyspark.sql.functions import explode

args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH', 'S3_TARGET_PATH2'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

schema = StructType([
    StructField("Id", StringType(), True),
    StructField("Nome", StringType(), True),
    StructField("Produtor", ArrayType(StringType()), True),
    StructField("Popularidade", DoubleType(), True),  # Alterado para DoubleType para maior precisão
    StructField("Duracao", IntegerType(), True),
    StructField("Orcamento", IntegerType(), True),
    StructField("Receita", IntegerType(), True)
])

dataframe = spark.read.json(args['S3_INPUT_PATH'], schema=schema)

dataframe = dataframe.withColumn("Duracao", dataframe["Duracao"].cast("int"))
dataframe = dataframe.withColumn("Orcamento", dataframe["Orcamento"].cast("int"))
dataframe = dataframe.withColumn("Receita", dataframe["Receita"].cast("int"))
dataframe = dataframe.withColumn("Popularidade", dataframe["Popularidade"].cast("double"))

exploded_df = dataframe.select("Id", explode("Produtor").alias("Producer"))
exploded_df.write.parquet(args['S3_TARGET_PATH2'], mode='overwrite')

other_columns_df = dataframe.select([column for column in dataframe.columns if column != "Produtor"])

other_columns_df.write.parquet(args['S3_TARGET_PATH'], mode='overwrite')

job.commit()
