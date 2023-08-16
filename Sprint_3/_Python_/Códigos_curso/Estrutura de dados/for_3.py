# For em dicionários

produto = {'nome': 'todynho', 'preço': 5.99,
            'validade': '11/28', 'marca': 'toddy'}

# Acessar keys

for chave in produto:
    print(chave)

# Acessar values

for valor in produto.values():
    print(valor)

# Acessar chaves e valores

for chave, valor in produto.items():
    print(f'{chave} = {valor}')

# OBS: Os valores de chave e valor ficam disponíveis
# depois da passagem pelo for, sendo as últimas informações
# de cada um

print(chave, valor)