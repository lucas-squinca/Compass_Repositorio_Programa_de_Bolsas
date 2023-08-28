"""
A coluna #1 Movie contém o filme de maior bilheteria em que o ator atuou. 
Realize a contagem de aparições destes filmes no dataset, listando-os ordenados 
pela quantidade de vezes em que estão presentes. 
Considere a ordem decrescente e, em segundo nível, o nome do  filme.

Ao escrever no arquivo, considere o padrão de saída 
<sequencia> - O filme <nome filme> aparece <quantidade> vez(es) no dataset, 
adicionando um resultado a cada linha.
"""

with open('actors.csv', 'r') as arquivo:
    with open('etapa_4.txt', 'w') as saida:
        linhas = arquivo.readlines()
        lista_filmes = {}
        soma = 0
        for linha in linhas[1:]:
            dados = linha.strip().rsplit(",", 5)
            if dados[4] in lista_filmes:
                lista_filmes[dados[4]] += 1
            else:
                 lista_filmes[dados[4]] = 1
        
        filmes_ordenados = sorted(lista_filmes.items())
        for i in range(len(filmes_ordenados)):
            for j in range(i + 1, len(filmes_ordenados)):
                if filmes_ordenados[i][1] < filmes_ordenados[j][1] or (filmes_ordenados[i][1] == filmes_ordenados[j][1] and filmes_ordenados[i][0] > filmes_ordenados[j][0]):
                    filmes_ordenados[i], filmes_ordenados[j] = filmes_ordenados[j], filmes_ordenados[i]

        for indice, (filme, quantidade) in enumerate(filmes_ordenados):
            print(f" {indice} - O filme '{filme}' aparece {quantidade} vez(es) no dataset", file= saida)