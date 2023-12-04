import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_TARGET_PATH'])

target_path = args['S3_TARGET_PATH']

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

dynamic_frame = glueContext.create_dynamic_frame.from_catalog(database = "tabela-desafio", table_name = "producers")
df = dynamic_frame.toDF()
df.createOrReplaceTempView('temp_df')

dim_produtor = spark.sql("""
    SELECT 
        id as id_produtor,
        producer as produtores
    FROM temp_df
""")

glueContext.write_dynamic_frame.from_options(
frame = dynamic_frame.fromDF(dim_produtor, glueContext, "dim_produtor"),
connection_type = "s3",
connection_options = {"path": target_path},
format = "parquet"
)

job.commit()