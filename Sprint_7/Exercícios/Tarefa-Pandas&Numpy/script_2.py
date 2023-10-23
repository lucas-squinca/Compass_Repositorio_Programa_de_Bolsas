"""
Apresente a média da coluna contendo o número de filmes.
"""

import pandas as pd

dados = pd.read_csv('actors.csv')

media_numero_de_filmes = dados['Number of Movies'].mean()

print(f"A média da coluna do número de filmes do arquivo actors.csv é {media_numero_de_filmes}")