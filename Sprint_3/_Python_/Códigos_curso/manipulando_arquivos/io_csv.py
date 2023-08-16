'''
Importando o csv, não precisamos mais fazer todo aquele
tratamento com .strip() e .split(',').
Ele já reconhece que estamos trabalhando com um arquivo .csv
e automaticamente o formata.
'''

import csv

with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade {}'.format(*pessoa))