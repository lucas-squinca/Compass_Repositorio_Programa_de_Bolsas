'''
Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor,
  Truese a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
    liga(): muda o estado da lâmpada para ligada
    desliga(): muda o estado da lâmpada para desligada
    esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário

Para testar sua classe:
    Ligue a Lampada
    Imprima: A lâmpada está ligada? True
    Desligue a Lampada
    Imprima: A lâmpada ainda está ligada? False
'''

class Lampada():
    def __init__(self, bools):
        self.ligada = True
        self.estado = None
        self.desligada = False
        
    def liga(self):
        self.estado = 'ligada'
    
    def desliga(self):
        self.estado = 'desligada'
    
    def esta_ligada(self):
        if self.estado == 'ligada':
            return True
        else:
            return False


if __name__ == '__main__':
    lampada = Lampada(None)
    lampada.liga()
    print(f'A lâmpada está ligada? {lampada.esta_ligada()}')
    lampada.desliga()
    print(f'A lâmpada ainda está ligada? {lampada.esta_ligada()}')
