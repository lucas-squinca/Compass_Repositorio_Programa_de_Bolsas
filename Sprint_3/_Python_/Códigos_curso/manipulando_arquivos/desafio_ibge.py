
with open('desafio-ibge.csv') as arquivo:
    for registro in arquivo:
        print('{8}: {3}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('O arquivo já está fechado')