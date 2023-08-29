from functools import reduce

pessoas = [
    {'nome': 'Pedro', 'idade': 17},
    {'nome': 'Lucas', 'idade': 23},
    {'nome': 'Maria', 'idade': 25},
    {'nome': 'Arthur', 'idade': 7},
    {'nome': 'Israel', 'idade': 87},
    {'nome': 'Lúcia', 'idade': 15},
]

soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
print(soma_idades)