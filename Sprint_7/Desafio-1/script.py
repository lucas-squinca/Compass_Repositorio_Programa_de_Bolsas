import boto3
import os
import csv
from datetime import datetime

aws_access_key = 'AKIAYAQIXF4HKRCGTD7X'
aws_secret_key = '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'
aws_bucket_name = 'desafio-aws-compass-lucas'
data_dir = 'Raw/Local/CSV' 

movies_file = 'movies.csv'
series_file = 'series.csv'

today = datetime.now()
year = today.year
month = today.strftime("%m")
day = today.strftime("%d")

s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

def upload_to_s3(file_path, s3_key):
    s3.upload_file(file_path, aws_bucket_name, s3_key)

movies_s3_key = f"{data_dir}/Movies/{year}/{month}/{day}/{movies_file}"
upload_to_s3(movies_file, movies_s3_key)

series_s3_key = f"{data_dir}/Series/{year}/{month}/{day}/{series_file}"
upload_to_s3(series_file, series_s3_key)

print("Desafio concluído com sucesso!")