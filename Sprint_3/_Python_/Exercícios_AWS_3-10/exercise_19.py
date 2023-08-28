import random

random_list = random.sample(range(500), 50)

def media(lista):
    tam = len(lista)
    soma = sum(lista)
    media = soma / tam

    return media

def min(lista):
    tam = len(lista)
    min = lista[0]
    for i in range(tam):
        if min > lista[i]:
            min = lista[i]
    return min


def max(lista):
    tam = len(lista)
    max = lista[0]
    for j in range(tam):
        if max < lista[j]:
            max = lista[j]
    return max

def mediana(lista):
    lista_ordenada = sorted(lista)
    tam = len(lista_ordenada)
    if tam % 2 == 0:
        mediana = (lista_ordenada[tam // 2] + lista_ordenada[(tam // 2) - 1]) / 2
    else:
        mediana = lista_ordenada[(tam // 2) - 1]
    return mediana

mediana = mediana(random_list)
media = media(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')