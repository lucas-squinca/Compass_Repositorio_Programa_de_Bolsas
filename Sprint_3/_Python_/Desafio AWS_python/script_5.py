"""
Apresente a lista dos atores ordenada pela receita 
bruta de bilheteria de seus filmes (coluna Total Gross), em ordem decrescente.

Ao escrever no arquivo, considere o padrão de saída 
<nome do ator> -  <receita total bruta>, adicionando um resultado a cada linha.
"""

with open('actors.csv') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        atores_gross = [(linha.strip().rsplit(",", 5)[0], float(linha.strip().rsplit(",", 5)[1])) for linha in linhas[1:]]
        n = len(atores_gross)
    for i in range(n):
        for j in range(0, n-i-1):
            if atores_gross[j][1] < atores_gross[j+1][1]:
                atores_gross[j], atores_gross[j+1] = atores_gross[j+1], atores_gross[j]

with open("etapa_5.txt", "w") as saida:
    for ator, gross in atores_gross:
        print(f"{ator} - R${gross}", file= saida)
arquivo.close()