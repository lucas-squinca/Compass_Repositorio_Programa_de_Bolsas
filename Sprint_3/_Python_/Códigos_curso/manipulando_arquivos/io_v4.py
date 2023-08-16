# Try: usado para que o programa 'tente' rodar o código,
# se der algum erro ou não, o bloco de comando que está em
# 'finally' sempre será executado;
# Usamos o 'finally' nesse caso para garantir que o arquivo
# será fechado;

try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
finally:
    arquivo.close()

if arquivo.closed:
    print('Arquivo já foi fechado!')