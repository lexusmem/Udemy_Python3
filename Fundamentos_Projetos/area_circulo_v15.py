#! python
# Shibang - Indicação do interpretador que será utilizado p executar o script

# Importação da função DEF "pi" do modulo "math"
from math import pi
import sys
import errno

# Criação de função DEF
# Definir o parametro que vou receber dentro das ()


class TermialColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def help():
    print("É necessario informar o raio do circulo.")
    print(f'Sintaxe correta: {sys.argv[0][2:]} <valor do raio>')


def circulo(raio):
    return pi * float(raio)**2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
        # Ou poderia utilizar sys.exit(1) parar de executar pois consta erro.

    if not sys.argv[1].isnumeric():
        help()
        print(TermialColor.ERRO + "O raio deve ser um valor númerico." +
              TermialColor.NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print(f'Area do cirulo é {area:.4f}')
