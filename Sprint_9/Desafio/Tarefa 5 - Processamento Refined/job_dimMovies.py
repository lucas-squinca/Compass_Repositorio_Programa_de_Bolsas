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

dynamic_frame = glueContext.create_dynamic_frame.from_catalog(database = "tabela-desafio", table_name = "csvcsv")
df = dynamic_frame.toDF()
df.createOrReplaceTempView('temp_df')
dynamic_frame2 = glueContext.create_dynamic_frame.from_catalog(database = "tabela-desafio", table_name = "dados_filmes")
df2 = dynamic_frame2.toDF()
df2.createOrReplaceTempView('temp_df2')

dim_movies = spark.sql("""
    SELECT DISTINCT
        d2.id as id_movie,
        d2.nome as titulo_principal,
        d1.anolancamento as ano_lancamento,
        d1.tempominutos as tempo_minutos
    FROM temp_df2 as d2
    INNER JOIN temp_df as d1 on d2.id = d1.id
""")

glueContext.write_dynamic_frame.from_options(
frame = dynamic_frame.fromDF(dim_movies, glueContext, "dim_movies"),
connection_type = "s3",
connection_options = {"path": target_path},
format = "parquet"
)

job.commit()