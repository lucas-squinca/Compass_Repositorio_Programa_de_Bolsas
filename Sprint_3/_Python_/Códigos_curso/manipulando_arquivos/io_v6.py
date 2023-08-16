'''
Escrevendo arquivo com base na leitura...
Com um segundo with abrindo um arquivo 'pessoas.txt' e
selecionando a função 'w' (write) criamos esse arquivo
com código python (mágica)
'''

with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('O arquivo já está fechado!')

if saida.closed:
    print('O arquivo de saída já está fechado!')