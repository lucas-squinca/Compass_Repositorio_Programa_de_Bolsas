def soma_string(string):
    soma = 0
    string = string.split(',')
    for i in string:
        soma = soma + int(i)
    return soma

string = "1,3,4,6,10,76"
soma = soma_string(string)
print(soma)