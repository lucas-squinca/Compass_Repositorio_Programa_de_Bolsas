import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import explode, split, array_contains
from pyspark.sql.types import ArrayType, StringType

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH', 'S3_TARGET_PATH2'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

dynamic_frame = glueContext.create_dynamic_frame.from_catalog(database = "tabela-desafio", table_name = "csvcsv")
df = dynamic_frame.toDF()

df = df.withColumn("genero", split(df["genero"], ",").cast(ArrayType(StringType())))
df = df.filter(array_contains(df["genero"], "Fantasy"))

df = df.withColumn("notamedia", df["notamedia"].cast("int"))
df = df.withColumn("tempominutos", df["tempominutos"].cast("int"))
df = df.withColumn("anolancamento", df["anolancamento"].cast("int"))

exploded_df = df.select("id", explode("genero").alias("genero"))
exploded_df.write.parquet(args['S3_TARGET_PATH'], mode='overwrite')

other_columns_df = df.select([column for column in df.columns if column != "genero"])
other_columns_df.write.parquet(args['S3_TARGET_PATH2'], mode='overwrite')

job.commit()
