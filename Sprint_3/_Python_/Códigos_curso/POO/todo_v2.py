from datetime import datetime

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def adicionar(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao[0]]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluído)' if self.feito else '')
    

def main():
    casa = Projeto('Tarefas de casa')
    casa.adicionar('Passar roupa')
    casa.adicionar('Lavar prato')
    print(casa)

    #casa.procurar('Lavar prato').concluir() # .concluir não está funcionado
    for tarefa in casa.tarefas:
        print(f'- {tarefa}')

    
    mercado = Projeto('Compras Mercado')
    mercado.adicionar('Maçã')
    mercado.adicionar('Manteiga')
    mercado.adicionar('Macarrão')
    print(mercado)
    for tarefa in mercado.tarefas:
        print(f'- {tarefa}')

if __name__ == '__main__':
    main()