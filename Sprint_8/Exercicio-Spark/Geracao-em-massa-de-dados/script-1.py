"""
Em Python, declare e inicialize uma lista contendo 250 inteiros obtidos de forma aleatória.
Após, aplicar o método reverse sobre o conteúdo da lista e imprimir o resultado.
"""

import random
import sys

lista_random = []
for i in range(250):
    lista_random.append(random.randint(1, sys.maxsize))

lista_invertida = sorted(lista_random, reverse=True)

print(lista_invertida)