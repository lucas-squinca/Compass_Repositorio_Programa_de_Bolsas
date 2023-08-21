
from datetime import datetime
from loja import Cliente, Vendedor, Compra

def main():
    cliente = Cliente('Mariana Silva', 47)
    vendedor = Vendedor('Pedro Garrido', 36, 5000)
    compra1 = Compra(cliente, datetime.now(), 512)
    compra2 = Compra(cliente, datetime(2018, 6, 7), 586)
    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)
    print(f'Cliente: {cliente}', '(adulto)' if cliente.is_adulto() else '')
    print(f'Última compra: {cliente.get_data_ultima_compra()}')


    if __name__ == '__main__':
        main()
