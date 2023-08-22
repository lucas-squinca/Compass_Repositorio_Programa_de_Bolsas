lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def sem_duplicatas(lista):
    lista_setada = set(lista)
    return lista_setada

def main():
    print(sem_duplicatas(lista))

print(main())