#! python
# Shibang - Indicação do interpretador que será utilizado p executar o script

from math import pi
# Forma para importar apenas o PI do modulo Math

# Irei verificar com IF se o nome do modulo é o pricipal
# Para poder executar o codigo de calculo da area
if __name__ == '__main__':
    print('Nome do Módulo: ', __name__)
    raio = input('Informe o Raio: ')
    area = pi * float(raio)**2
    print(f'Area do circulo: {area:.2f}')
