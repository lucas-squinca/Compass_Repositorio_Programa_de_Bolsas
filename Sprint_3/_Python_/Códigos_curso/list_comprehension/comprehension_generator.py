generator = (i ** 2 for i in range(11) if i % 2 == 0)
print(next(generator)) # Saída 0
print(next(generator)) # Saída 4
print(next(generator)) # Saída 16
print(next(generator)) # Saída 36
print(next(generator)) # Saída 64
print(next(generator)) # Saída 100

# Um generator ocupa menos espaço na memória;
# Um generator gera os dados sob demanda;

