lista_1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {'nome': 'Joao', 'idade': 14},
    {'nome': 'Maria', 'idade': 45},
    {'nome': 'Eduardo', 'idade': 21}
]
so_nomes = map(lambda p: p['nome'], lista_2)
print(list(so_nomes))

so_idades = map(lambda i: i['idade'], lista_2)
print(list(so_idades))

frases = map(lambda i: f"{i['nome']} possui {i['idade']} anos", lista_2)
print(list(frases))