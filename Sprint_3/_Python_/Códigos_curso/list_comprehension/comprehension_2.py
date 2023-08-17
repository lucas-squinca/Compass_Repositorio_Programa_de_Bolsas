# Pegar os valores de 1 a 10 somente pares:

pares = [i for i in range(1, 11) if i % 2 == 0]
print(pares)

# Sem list comprehension

pares = []
for i in range(1, 11):
    if i % 2 == 0:
        pares.append(i)
print(pares)