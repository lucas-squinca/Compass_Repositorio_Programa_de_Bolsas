# Exemplos simples:
# Podemos chamar uma função com parâmetros para dentro
# de outra função!!

def executar(funcao):
    funcao()


def bom_dia():
    print('Bom dia!')

def boa_tarde():
    print('Boa tarde!')

if __name__ == '__main__':
    executar(bom_dia)
    executar(boa_tarde)