"""
Apresente o nome do ator/atriz com a maior média por filme.
"""

import pandas as pd

dados = pd.read_csv('actors.csv')

maior_media_por_filme = dados[dados['Average per Movie'] == dados['Average per Movie'].max()]

ator_com_maior_media = maior_media_por_filme['Actor'].values[0]
media_do_ator = maior_media_por_filme['Average per Movie'].values[0]

print(f"O nome do ator ou atriz com a maior média por filmes é {ator_com_maior_media}, cuja média é {media_do_ator}")