#! python
# Shibang - Indicação do interpretador que será utilizado p executar o script

# Importação da função DEF "pi" do modulo "math"
from math import pi
import sys

# Criação de função DEF
# Definir o parametro que vou receber dentro das ()


def help():
    print("É necessario informar o raio do circulo.")
    print(f'Sintaxe correta: {sys.argv[0][2:]} <valor do raio>')


def circulo(raio):
    return pi * float(raio)**2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print(f'Area do cirulo é {area:.4f}')
