"""
Apresente o nome do(s) filme(s) mais 
frequente(s) e sua respectiva frequência.
"""

import pandas as pd

i = 1;
dados = pd.read_csv('actors.csv')

filmes_mais_frequentes = dados['#1 Movie'].value_counts().head(5)

for nome_filme, frequencia in filmes_mais_frequentes.items():
    print(f'{i}° Filme mais frequente: {nome_filme}, o qual aparece {frequencia} vezes no arquivo')
    i += 1