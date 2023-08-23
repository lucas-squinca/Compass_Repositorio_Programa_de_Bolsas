class Ordenadora:
    def __init__(self, ListaBaguncada):
        self.ListaBaguncada = ListaBaguncada

    def ordenacaoCrescente(self):
        return sorted(self.ListaBaguncada)

    def ordenacaoDecrescente(self):
        return sorted(self.ListaBaguncada, reverse=True)
    
crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])

print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())


