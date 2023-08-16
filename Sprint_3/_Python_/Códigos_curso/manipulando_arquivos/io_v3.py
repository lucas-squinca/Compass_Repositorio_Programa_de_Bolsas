# Usando a função .strip(), conseguimos retirar o
# espaçamento entre as linhas;

arquivo = open('pessoas.csv')

for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()