from app_desafio.utils.gerador import novo_nome
from app_desafio.negocio import nome_existe
from app_desafio.negocio.backend import add_nome

def main():
    while True:
        nome = novo_nome()
        if not nome_existe(nome):
            add_nome(nome)
            break

    print(f'Criado novo nome de testes: "{nome}"')



if __name__ == '__main__':
    main()