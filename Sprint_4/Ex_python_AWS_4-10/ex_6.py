def maiores_que_media(conteudo:dict)->list:
    lista_result = []
    media = sum(conteudo.values()) / len(conteudo.keys())
    for chave, valor in conteudo.items():
        if valor > media:
            lista_result.append((chave, valor))
            
    lista_result = sorted(lista_result, key=lambda x: x[1])

    return lista_result

if __name__ == '__main__':
    conteudo = {
        "arroz": 4.99,
        "feijão": 3.49,
        "macarrão": 2.99,
        "leite": 3.29,
        "pão": 1.99
    }

    lista_final = maiores_que_media(conteudo)
    print(lista_final)

    
