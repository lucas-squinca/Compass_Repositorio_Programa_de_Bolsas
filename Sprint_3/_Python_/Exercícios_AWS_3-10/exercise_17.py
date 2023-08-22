lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def dividir_lista(lista):
    tam = len(lista) // 3
    lista_1 = lista[0:tam]
    lista_2 = lista[tam:tam*2]
    lista_3 = lista[tam*2:]
    
    return f'{lista_1} {lista_2} {lista_3}'

print(dividir_lista(lista))



