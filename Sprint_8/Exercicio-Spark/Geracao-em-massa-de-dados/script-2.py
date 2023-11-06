"""
Em Python, declare e inicialize uma lista contendo o nome de 20 animais.
Ordene-os em ordem crescente e itere sobre os itens, imprimindo um a um (você pode utilizar list comprehension aqui).
Na sequência, armazene o conteúdo da lista em um arquivo de texto, um item em cada linha, no formato CSV.
"""

lista_animais = ['cachorro', 'gato', 'elefante', 'zebra', 'macaco', 'rinoceronte', 'hipopotamo', 'avestruz', 'cobra', 
                 'teiu', 'leao', 'tigre', 'leopardo', 'girafa', 'urubu', 'canguru', 'tucano', 'arara-azul', 'escorpiao', 'aranha']


print(lista_animais)

lista_ordenada = sorted(lista_animais)

print(lista_ordenada)

[print(animal) for animal in lista_ordenada]

with open("lista_animais.csv", 'w') as lista:
    for animal in lista_ordenada:
        lista.write(animal + "\n")

lista.close()