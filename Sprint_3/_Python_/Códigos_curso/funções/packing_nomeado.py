# **kwargs
def resultado_f1(**podio):
    for posicao, piloto in podio.items():
        print(f'{posicao} -> {piloto}')

if __name__ == '__main__':
    resultado_f1(primeiro='L. Hamilton',
                 segundo='M. Verstappen',
                 terceiro='S. Vettel')