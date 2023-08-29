from primeira_classe import dobro, quadrado

def processar(titulo, lista, funcao):
    print(f'Processando {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))

if __name__ == '__main__':

    # Neste caso, passamos uma função dentro de outra função e executamos o código com sucesso
    processar('Dobros de 1 a 10', range(1, 11), dobro)
    processar('Quadrados de um a 10', range(1, 11), quadrado)