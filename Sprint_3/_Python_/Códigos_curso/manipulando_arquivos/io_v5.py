'''
Neste caso, usamos o with para simplificar o nosso código,
já que não precisamos atribuir o nosso arquivo .csv para 
uma variável 'arquivo', nem mesmo fechar o arquivo manualmente
por meio do arquivo.close();
'''

# + PRÁTICO

with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('O arquivo já está fechado!')