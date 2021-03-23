#! python
# Shibang - Indicação do interpretador que será utilizado p executar o script

from math import pi

# Criação de função DEF
# Definir o parametro que vou receber dentro das ()


def circulo(raio):
    area = pi * float(raio)**2
    print(f'Area do circulo: {area:.2f}')


if __name__ == '__main__':
    raio = input('Informe o Raio: ')
    circulo(raio)
