"""
Apresente o ator/atriz com maior número de filmes e a respectiva quantidade.
A quantidade de filmes encontra-se na coluna Number of Movies do arquivo.
"""

with open('actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()
    ator_max = ''
    qtd_filmes = 0

    for linha in linhas[1:]:
        dados = linha.strip().rsplit(",", 5)
        ator = dados[0]
        num_filmes = int(dados[2])
        if num_filmes > qtd_filmes:
            ator_max = ator
            qtd_filmes = num_filmes
    
with open('etapa_1.txt', 'w') as saida:
    print(f'O ator que possui a maior quantidade de filmes e {ator_max}, com respectivamente {qtd_filmes} filmes', file=saida)

arquivo.close()