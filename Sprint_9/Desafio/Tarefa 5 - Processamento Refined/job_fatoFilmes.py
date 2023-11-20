import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import monotonically_increasing_id, concat

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

dynamic_frame1 = glueContext.create_dynamic_frame.from_catalog(database = "refined", table_name = "dimmovies")
df1 = dynamic_frame1.toDF()
df1.createOrReplaceTempView('temp_movies')

dynamic_frame3 = glueContext.create_dynamic_frame.from_catalog(database = "refined", table_name = "dimprodutores")
df3 = dynamic_frame3.toDF()
df3.createOrReplaceTempView('temp_producers')

dynamic_frame4 = glueContext.create_dynamic_frame.from_catalog(database = "refined", table_name = "dimgenero")
df4 = dynamic_frame4.toDF()
df4.createOrReplaceTempView('temp_genero')

dynamic_frame2 = glueContext.create_dynamic_frame.from_catalog(database = "tabela-desafio", table_name = "dados_filmes")
df2 = dynamic_frame2.toDF()

df2 = df2.withColumn("id_indice", monotonically_increasing_id())

df2.createOrReplaceTempView('temp_df2')

fato_filmes = spark.sql("""
    SELECT DISTINCT
        d2.id_indice as id,
        d2.popularidade as popularidade,
        d1.notamedia as nota_media,
        d2.orcamento as orcamento,
        d2.receita as receita,
        mov.id_movie as id_movies,
        pro.id_produtor as id_produtores,
        gen.id_genero as id_genero
    FROM temp_df2 as d2
    INNER JOIN temp_df as d1 on d2.id = d1.id
    INNER JOIN temp_genero as gen on d2.id = gen.id_genero
    INNER JOIN temp_producers pro on d2.id = pro.id_produtor
    INNER JOIN temp_movies mov on d2.id = mov.id_movie
""")

glueContext.write_dynamic_frame.from_options(
frame = dynamic_frame.fromDF(fato_filmes, glueContext, "fato_filmes"),
connection_type = "s3",
connection_options = {"path": target_path},
format = "parquet"
)

job.commit()