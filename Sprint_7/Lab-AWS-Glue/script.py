import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import upper

##@params: [JOB_NAME]

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

df = glueContext.create_dynamic_frame.from_options("s3",{"paths": [source_file]},"csv",{"withHeader": True, "separator":","},)

df.printSchema()

data_frame = df.toDF()

df_upper = data_frame.withColumn("nome", upper(data_frame["nome"]))
df_upper.show()

count = df.count()
print("Contagem de linhas: ", count)

grouped_data_frame = data_frame.groupBy(["ano", "sexo"]).count()
sorted_data_frame = grouped_data_frame.orderBy(["ano", "sexo"], ascending=[False, True])
sorted_data_frame.show()

female_df = data_frame.filter(data_frame['sexo'] == 'F')
most_common_name_f = female_df.orderBy('total', ascending=False).first()
print(f"O nome feminino com mais registros é:{most_common_name_f['nome']}, cujo ano de ocorrência é {most_common_name_f['ano']}")

male_df = data_frame.filter(data_frame['sexo'] == 'M')
most_common_name_m = male_df.orderBy('total', ascending=False).first()
print(f"O nome masculino com mais registros é:{most_common_name_m['nome']}, cujo ano de ocorrência é {most_common_name_m['ano']}")

yearly_counts = df.groupBy('ano', 'sexo').count()
result = yearly_counts.orderBy('ano').limit(10)
result.show()

dynamic_frame_upper = df_upper.fromDF(df_upper, glueContext, "dynamic_frame_upper")

glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame_upper,
    connection_type="s3",
    connection_options={"path": target_path},
    format="json"
)

job.commit()