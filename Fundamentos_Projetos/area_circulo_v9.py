#! python
# Shibang - Indicação do interpretador que será utilizado p executar o script

from math import pi

# Criação de função DEF
# Definir o parametro que vou receber dentro das ()


def circulo(raio):
    return pi * float(raio)**2


if __name__ == '__main__':
    raio = input('Informe o Raio: ')
    area = circulo(raio)
    print(type(area))
    print(f'Area do cirulo é {area:.2f}')
