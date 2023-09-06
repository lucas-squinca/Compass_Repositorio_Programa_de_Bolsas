with open('estudantes.csv', 'r') as arquivo:
    linhas = arquivo.readlines()
    dados_estudantes = []
    for linha in linhas:
        dados = linha.strip().split(",")
        dados_int = []
        for dado in dados[1:]:
            dados_int.append(int(dado))
        ordenado = sorted(dados_int, reverse=True)
        tres_maiores = list(map(lambda x: x, ordenado[:3]))
        media = (int(tres_maiores[0]) + int(tres_maiores[1]) + int(tres_maiores[2])) / 3
        media_arredondada = round(media, 2)
        
        dados_estudantes.append((dados[0], tres_maiores, media_arredondada))

    dados_estudantes = sorted(dados_estudantes, key=lambda x: x[0])
        
    for estudante in dados_estudantes:
        print(f'Nome: {estudante[0]} Notas: {estudante[1]} Média: {estudante[2]}')
    