def pares_ate(n:int):
    for numero in range(2, n + 1, 2):
        yield numero
    
generator = pares_ate(8)
print(next(generator))