# Criação de classe
# Self é o objeto que naquele momento está em execução na função;
class Data: # No python, podemos ter apenas UM construtor;
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        

    def __str__(self): # Todo parâmetro inicia-se com self;
        return f'{self.dia}/{self.mes}/{self.ano}'

# Criação de objeto a partir da classe
d1 = Data(5, 12, 2019)
#d1.dia = 5
#d1.mes = 12
#d1.ano = 2021
print(d1)


d2 = Data(7, 4, 2021)
#d2.dia = 7
#d2.mes = 4
#d2.ano = 2020
print(d2)