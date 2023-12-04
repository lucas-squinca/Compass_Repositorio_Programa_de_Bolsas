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

dynamic_frame = glueContext.create_dynamic_frame.from_catalog(database = "tabela-desafio", table_name = "genero")
df = dynamic_frame.toDF()
df.createOrReplaceTempView('temp_df')
dynamic_frame2 = glueContext.create_dynamic_frame.from_catalog(database = "tabela-desafio", table_name = "dados_filmes")
df2 = dynamic_frame2.toDF()
df2.createOrReplaceTempView('temp_df2')


dim_genero = spark.sql ("""
    SELECT DISTINCT
        df1.id as id_genero,
        df1.genero as generos
    FROM temp_df2 as df2
    INNER JOIN temp_df as df1 on df2.id = df1.id

""")
                                   
dynamic_frame = dynamic_frame.select_fields(["id_genero", "genero"])
glueContext.write_dynamic_frame.from_options(
frame = dynamic_frame.fromDF(dim_genero, glueContext, "dim_genero"),
connection_type = "s3",
connection_options = {"path": target_path},
format = "parquet"
)

job.commit()