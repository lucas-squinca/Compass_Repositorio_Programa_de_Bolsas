from datetime import datetime, timedelta

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def adicionar(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao[0]]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'

class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluído)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')
        
        return f'{self.descricao} ' + ' '.join(status)
    

def main():
    casa = Projeto('Tarefas de casa')
    casa.adicionar('Passar roupa,', datetime.now())
    casa.adicionar('Lavar prato', datetime.now() + timedelta(days=3, minutes=12))
    print(casa)

    #casa.procurar('Lavar prato').concluir() # .concluir não está funcionando
    for tarefa in casa:
        print(f'- {tarefa}')

    
    mercado = Projeto('Compras Mercado')
    mercado.adicionar('Maçã')
    mercado.adicionar('Manteiga')
    mercado.adicionar('Macarrão', datetime.now() + timedelta(days=4, minutes=45))
    print(mercado)
    for tarefa in mercado:
        print(f'- {tarefa}')

if __name__ == '__main__':
    main()