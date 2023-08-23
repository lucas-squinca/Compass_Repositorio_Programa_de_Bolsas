class Aviao:

    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = 'Azul'

lista_avioes = []
modelos = ['BOEING456', 'Embraer Praetor 600', 'Antonov An-2']
velocidades = [1500, 863, 258]
capacidades = [400, 14, 12]
j = 0;
for i in [modelos, velocidades, capacidades]:
    mod = modelos[j]
    vel = velocidades[j]
    cap = capacidades[j]
    aviao = Aviao(mod, vel, cap)
    lista_avioes.append(aviao)
    j += 1

for aviao in lista_avioes:
    print(f'O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima} km/h, capacidade para {aviao.capacidade} passageiros e é da cor {aviao.cor}.')