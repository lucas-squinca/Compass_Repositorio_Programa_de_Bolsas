"""
Apresente a média de receita de bilheteria bruta dos principais filmes, considerando todos os atores.
Estamos falando aqui da média da coluna Gross.
"""

with open('actors.csv', 'r') as arquivo:
    with open("etapa_2.txt", "w") as saida:
        linhas = arquivo.readlines()
        soma = 0
        ator = ""
        for linha in linhas[1:]:
            dados = linha.strip().rsplit(",", 5)
            gross = float(dados[5])
            soma += gross
        
        qtd = (len(linhas) - 1)
        media = soma / qtd
        ator = dados[0]
        print(f"A media dos filmes e {media:.2f}", file= saida)