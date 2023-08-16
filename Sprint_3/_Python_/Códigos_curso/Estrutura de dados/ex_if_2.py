def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'menor de idade'
    elif idade in range(18, 65):
        return 'adulto'
    elif idade in range(65, 100):
        return 'idoso'
    elif idade >= 100:
        return 'Centenária'
    else:
        return 'idade inválida'
    
if __name__ == '__main__':
    for idade in (15, 17, 35, 80, 110, -2):
        print(f'{idade}: {faixa_etaria(idade)}')