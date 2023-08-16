# Nova versão: mais simples e rápida;
# Não lê todo o arquivo;
# Interessante quando ler arquivos grandes;
# Não carrega todo oa arquivo na memória, + rápido;

arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome: {} Idade {}'.format(*registro.split(',')))
arquivo.close()