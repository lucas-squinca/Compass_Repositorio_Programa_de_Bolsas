def soma_2(a, b):
    return a + b
def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma

if __name__ == '__main__':
    # Packing
    print(soma_2(1, 2))
    print(soma_3(5, 4, 1))
    print(soma_n(1, 7))
    print(soma_n(1, 7, 4, 8, 5))

    # Unpacking
    nums = (1, 2, 3, 4)
    print(soma_n(*nums))