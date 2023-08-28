"""
Apresente o ator/atriz com a maior média de receita de bilheteria bruta por filme do conjunto de dados.
Considere a coluna Avarage per Movie para fins de cálculo.
"""

with open('actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()
    maior = 0
    ator = ""
    for linha in linhas[1:]:
        dados = linha.strip().rsplit(",", 5)
        if dados[3] > maior:
            maior = dados[3]
            ator = dados[0]

        

with open('etapa_3.txt', 'w') as saida:
    print(f'O ator com maior media de receita de bilheteria bruta por filme e {ator}', file=saida)
        