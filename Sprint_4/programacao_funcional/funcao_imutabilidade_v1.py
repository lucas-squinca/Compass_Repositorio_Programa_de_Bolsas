from functools import reduce
from operator import __add__

# Algumas funções que não alteram o valor da nossa variável:
valores = [30, 21, 47, 89, 56]
print(sorted(valores))
print(valores)

#valores.sort()
#print(valores)

print(min(valores))
print(max(valores))
print(sum(valores))
print(list(reversed(valores)))

# Podemos também basicamente usar dados imutáveis, como uma tupla;