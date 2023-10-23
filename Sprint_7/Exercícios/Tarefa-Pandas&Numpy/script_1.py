"""
Identifique o ator/atriz com maior número
de filmes e o respectivo número de filmes.
"""

import pandas as pd

dados = pd.read_csv('actors.csv')

ator_max = dados[dados['Number of Movies'] == dados['Number of Movies'].max()]

ator_nome = ator_max['Actor'].values[0]

numero_de_filmes = ator_max['Number of Movies'].values[0]

print(f"O ator com o maior número de filmes é {ator_nome} com respectivamente {numero_de_filmes} filmes")