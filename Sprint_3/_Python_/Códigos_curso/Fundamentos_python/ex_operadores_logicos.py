# Desafio operadores lógicos

trabalho_terca = True
trabalho_quinta = False

"""
Confirmando os dois: Tv 50' + sorvete;
Confirmando somente um: Tv 32' + sorvete;
Negando ambos: Ficar em casa;
"""

# Minha resposta

if trabalho_quinta and trabalho_terca:
    print("Tv 50' e sorvete")
elif trabalho_terca or trabalho_quinta:
    print("Tv 32' e sorvete")
else:
    print("Ficar em casa")

# Resposta esperada:

tv_50 = trabalho_quinta and trabalho_terca
tv_32 = trabalho_terca != trabalho_quinta
sorvete = trabalho_quinta or trabalho_terca
mais_saudavel = not sorvete

# Print usando formatação FORMAT
print('Tv50={} Tv32={} Sorvete={} Ficar em casa={}'
      .format(tv_50, tv_32, sorvete, mais_saudavel))
# Print usando formatação f''
print(f'Tv50={tv_50} Tv32={tv_32} Sorvete={sorvete} Ficar em casa={mais_saudavel}')