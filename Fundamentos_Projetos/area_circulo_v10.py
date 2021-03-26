#! python
# Shibang - Indicação do interpretador que será utilizado p executar o script

# Importação da função DEF "pi" do modulo "math"
from math import pi
import sys

# Criação de função DEF
# Definir o parametro que vou receber dentro das ()


def circulo(raio):
    return pi * float(raio)**2


if __name__ == '__main__':
    raio = sys.argv[1]
    area = circulo(raio)
    print(f'Area do cirulo é {area:.2f}')
