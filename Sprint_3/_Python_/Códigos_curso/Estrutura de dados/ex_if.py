'''
Faça uma função que dê como saída uma nota de A até E-
de acordo com a nota dada pelo usuário em número.
'''

# A = De 10.0 a 9.1
# A- = De 9.0 a 8.1
# B = De 8.0 a 7.1
# B- = De 7.0 a 6.1
# C = De 6.0 a 5.1
# C- = De 5.0 a 4.1
# D = De 4.0 a 3.1
# D- = De 3.0 a 2.1
# E = De 2.0 a 1.1
# E- = De 1.0 a 0.0

nota = float(input('Digite sua nota em número: '))

if nota <= 10.0 and nota > 9.0:
    print('A')
elif nota <= 9.0 and nota > 8.0:
    print('A-')
elif nota <= 8.0 and nota > 7.0:
    print('B')
elif nota <= 7.0 and nota > 6.0:
    print('B-')
elif nota <= 6.0 and nota > 5.0:
    print('C')
elif nota <= 5.0 and nota > 4.0:
    print('C-')
elif nota <= 4.0 and nota > 3.0:
    print('D')
elif nota <= 3.0 and nota > 2.0:
    print('D-')
elif nota <= 2.0 and nota > 1.0:
    print('E')
elif nota <= 1.0 and nota > 0.0:
    print('E-')
else:
    print('Nota inválida')

    