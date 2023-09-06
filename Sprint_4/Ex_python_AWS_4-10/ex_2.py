
def conta_vogais(texto:str)-> int:
    e_vogal = lambda x: x.lower() in 'aeiou'
    qtd_vogais = filter(e_vogal, texto.lower())
    soma_de_vogais = len(list(qtd_vogais))
    return soma_de_vogais



if __name__ == '__main__':
    string = input('Digite uma palavra: ')

    num_vogais = conta_vogais(string)
    print(num_vogais)