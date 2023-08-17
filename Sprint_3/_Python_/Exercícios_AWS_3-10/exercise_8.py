lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for i in range(6):
    if lista[i][::-1] == lista[i]:
        print(f'A palavra: {lista[i]} é um palíndromo\n')
    else:
        print(f'A palavra: {lista[i]} não é um palíndromo\n')