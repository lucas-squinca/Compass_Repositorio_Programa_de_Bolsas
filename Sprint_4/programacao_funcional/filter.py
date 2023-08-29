pessoas = [
    {'nome': 'Pedro', 'idade': 17},
    {'nome': 'Lucas', 'idade': 23},
    {'nome': 'Maria', 'idade': 25},
    {'nome': 'Arthur', 'idade': 7},
    {'nome': 'Israel', 'idade': 87},
    {'nome': 'Lúcia', 'idade': 15},
]
menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

maiores = filter(lambda p: p['idade'] > 18, pessoas)
print(list(maiores))

nome_grande = filter(lambda p: len(p['nome']) > 5, pessoas)
print(list(nome_grande))