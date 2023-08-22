
def potencia(num):
    return int(num) ** 2
    
def my_map(lista2, function):
    lista_nova = []
    for i in lista2:
        lista_nova.append(function(i))
    return lista_nova

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_map(lista, potencia))