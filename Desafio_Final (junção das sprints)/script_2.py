# Tentativa de criar uma função para ser usada na lambda -> Sem sucesso

import json
import datetime
import requests
import os
import boto3
import pandas as pd
from ratelimit import limits, sleep_and_retry

api_key = "minha_key_protegida"
bucket_s3 = "desafio-aws-compass-lucas"

def lambda_handler(event, context):
    process_data_tmdb('movies.csv', 'Filmes')

def catch_data(api_key, imdb_id, tipe_of_media):
    endpoint = 'movie'
    url = f'https://api.themoviedb.org/3/{endpoint}/{imdb_id}'
    response = requests.get(url, params={"api_key": api_key})

    if response.status_code == 200:
        tmdb_data = response.json()
        data_to_save = {
            'Id': tmdb_data['imdb_id'],
            'Nome': tmdb_data['title'],
            'Produtor': [produtor['name'] for produtor in tmdb_data.get('production_companies',[])],
            'Popularidade': tmdb_data['popularity'],
            'Duracao': tmdb_data['runtime'],
            'Orcamento': tmdb_data['budget'],
            'Receita': tmdb_data['revenue']
        }
        return data_to_save
    else:
        return None

@sleep_and_retry
@limits(calls=240, period=1)
def save_data_s3(data, bucket_name, archive):
    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket_name, Key=archive, Body=json.dumps(data))

def process_data_tmdb(archive, tipe_of_media):
    dataframe = pd.read_csv(archive, sep="|")
    dataframe = dataframe.drop_duplicates(subset=['id'])

    dataframe['genero'] = dataframe['genero'].fillna('')
    dataframe['genero'] = dataframe['genero'].str.split(',')

    fantasy_and_scifi = dataframe[dataframe['genero'].apply(lambda genres: 'Fantasy' in genres)]

    dictionary = fantasy_and_scifi.to_dict(orient='records')

    data_hr = datetime.datetime.now().strftime('%Y/%m/%d')
    type_lower = tipe_of_media.lower()

    list_of_media = []

    for information in dictionary:
        imdb_id = information['id']
        tmdb_data = catch_data(api_key, imdb_id, tipe_of_media)

        if tmdb_data:
            list_of_media.append(tmdb_data)

    batch_size = 100
    for batch_id, start in enumerate(range(0, len(list_of_media), batch_size), start=1):
        end = start + batch_size
        batch_info = list_of_media[start:end]

        folder_path = os.path.join(bucket_s3, 'Raw', 'TMDB', 'JSON', data_hr)
        os.makedirs(folder_path, exist_ok=True)
        name_archive = os.path.join(folder_path, f'{type_lower}_{batch_id}.json')
        save_data_s3(batch_info, bucket_s3, name_archive)
