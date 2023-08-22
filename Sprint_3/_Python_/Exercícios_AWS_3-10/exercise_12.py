import json

arquivo = open('person.json')
arquivo_lido = arquivo.read()
dados = json.loads(arquivo_lido)

print(dados)