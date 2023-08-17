generator = (i ** 2 for i in range(10) if i % 2 == 0)

for numero in generator:
    print(numero)

# Forma mais prática de acessar um generator, sem necessidade de da função next();
