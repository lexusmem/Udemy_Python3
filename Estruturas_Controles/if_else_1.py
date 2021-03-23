# Conceitos     Notas
# A             De 10,0 a 9,1
# A-            De 9,0 a 8,1
# B             De 8,0 a 7,1
# B-            De 7,0 a 6,1
# C             De 6,0 a 5,1
# C-            De 5,0 a 4,1
# D             De 4,0 a 3,1
# D-            De 3,0 a 2,1
# E             De 2,0 a 1,1
# E-            De 1,0 a 0,1

# Para nota maiores que 10 e menores que 0 será impresso "Nota Inválida."

import sys
import errno


class cores:
    ALERTA = '\033[91m'
    NORMAL = '\033[0m'


def erro():
    print('Valor Inválido! Não informado Valor.')
    print(cores.ALERTA + 'Digite um numero entre 10 e 0,1.' + cores.NORMAL)
    print(f'Sintaxe correta {sys.argv[0][2:]} <valor>.')


def errostr():
    print('Valor Inválido! Não informar Letras.')
    print(cores.ALERTA + 'Digite um numero entre 10 e 0,1.' + cores.NORMAL)
    print(f'Sintaxe correta {sys.argv[0][2:]} <valor>.')


def erro10():
    print('Valor Inválido! Maior que Dez.')
    print(cores.ALERTA + 'Digite um numero entre 10 e 0,1.' + cores.NORMAL)
    print(f'Sintaxe correta {sys.argv[0][2:]} <valor>.')


def erro0():
    print('Valor Inválido! Menor que Zero.')
    print(cores.ALERTA + 'Digite um numero entre 10 e 0,1.' + cores.NORMAL)
    print(f'Sintaxe correta {sys.argv[0][2:]} <valor>.')


def avaliacao(valor):
    nota = float(valor)

    if nota > 10:
        return erro10()
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0:
        return 'E-'
    elif nota <= 0:
        return erro0()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        erro()
        sys.exit(errno.EPERM)

    # Pegando dado digitado no terminal.
    valor = sys.argv[1]
    nota = avaliacao(valor)
    print(nota)

    # Solicitando digitação do dado.
    nota_informada = input(
        cores.ALERTA + 'Informe a nota do Aluno: ' + cores.NORMAL)
    nota_apurado = avaliacao(nota_informada)
    print(nota_apurado)
