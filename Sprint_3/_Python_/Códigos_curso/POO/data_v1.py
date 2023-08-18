# Criação de classe
# Self é o objeto que naquele momento está em execução na função;
class Data:
    def __str__(self): # Todo parâmetro inicia-se com self;
        return f'{self.dia}/{self.mes}/{self.ano}'

# Criação de objeto a partir da classe
d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2021
print(d1)


d2 = Data()
d2.dia = 7
d2.mes = 4
d2.ano = 2020
print(d2)