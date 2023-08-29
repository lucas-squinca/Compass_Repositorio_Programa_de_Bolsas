# Neste código, usamos as nossas funções como simples variáveis e as manipulamos.
def dobro(x):
    return x * 2

def quadrado(x):
    return x ** 2

if __name__ == '__main__':
    # Retorna alternadamente o dobro ou quadrado nos números de 1 a 10
    funcoes = [dobro, quadrado] * 5
    for funcoes, numero in zip(funcoes, range(1, 11)):
        print(f'O {funcoes.__name__} de {numero} é {funcoes(numero)}')
