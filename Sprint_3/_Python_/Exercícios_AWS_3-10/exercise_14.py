
def imprimir(*args, **kwargs):
    for i in args:
        print('{}'.format(i))
    for j in kwargs.values():
        print('{}'.format(j))

imprimir(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)