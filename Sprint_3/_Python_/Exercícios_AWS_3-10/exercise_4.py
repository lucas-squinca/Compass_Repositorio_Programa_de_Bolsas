
for i in range(1, 101):
    soma = 0
    for j in range(1, i + 1):
        if i % j == 0:
            soma = soma + 1

    if soma == 2:
        print(i)
    