
from functools import reduce

def calcula_saldo(lancamentos) -> float:
    def calcula_valor(lancamento):
        valor, tipo = lancamento
        if tipo == 'C':
            return int(valor)
        else:
            return int(-valor)

    valores = map(calcula_valor, lancamentos)
    saldo = reduce(lambda x, y: x + y, valores)

    return saldo



if __name__ == '__main__':
    lancamentos = [
        (200, 'D'),
        (300, 'C'),
        (100, 'C')
    ]

    result = calcula_saldo(lancamentos)
    print(result)