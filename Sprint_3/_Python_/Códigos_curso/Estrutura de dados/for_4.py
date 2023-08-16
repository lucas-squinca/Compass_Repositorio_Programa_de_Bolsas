'''
função sortedar_dado com números de 1 a 6;
For com range 1 a 6;
Se for impar, continue;
Se for par e for igual ao valor sorteado pela seleção
printar 'ACERTOU' e depois chamar o break;
Se não acertar chama o else: 'Não acertou o número';
'''

def sortear_dado(numero):
    from random import randint

    num_sorteado = randint(1, 6)

    for i in range(1, 7):
        if numero % 2 != 0:
            continue
        elif numero % 2 == 0 and numero == num_sorteado:
            return "Acertou!"
    else:
        return 'Não acertou o número'

if __name__ == '__main__':
    for j in range(1, 6):
        numero = int(input("Digite um número de 1 a 6: "))
        print(f'{sortear_dado(numero)}')

# Resposta esperada:

