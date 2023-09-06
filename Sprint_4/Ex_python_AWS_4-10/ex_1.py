'''
Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha.
Utilizando lambdas e high order functions,
apresente os 5 maiores valores pares e a soma destes.
Você deverá aplicar as seguintes funções no exercício:

- map
- filter
- sorted
- sum

Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):

- a lista dos 5 maiores números pares em ordem decrescente;
- a soma destes valores.
'''

with open("number.txt", "r") as arquivo:

    def pares(num):
        return filter(lambda x: x % 2 == 0, num)
    
    def ordem_decrescente(num):
        return sorted(num, reverse=True)
    
    def cinco_maiores(num):
        return list(map(lambda x: x , num[:5]))

    def soma(num):
        return sum(num)
    

    numeros = []
    linhas = arquivo.readlines()
    for linha in linhas[:]:
        dados = linha.strip()
        numeros.append(int(dados))

    numeros_pares = pares(numeros)
    num_pares_ordenados = ordem_decrescente(numeros_pares)
    lista_cinco_maiores = cinco_maiores(num_pares_ordenados)
    print(lista_cinco_maiores)
    somatorio = soma(lista_cinco_maiores)
    print(somatorio)
    