#! python
# Shibang - Indicação do interpretador que será utilizado p executar o script

from math import pi
# Forma para importar apenas o PI do modulo Math


print(f'Valor de Pi = {pi}')
print('Valor de Pi (4 casas decimais)= %.4f' % (pi))

raio = input('Informe o Raio: ')

area = pi * float(raio)**2
print(f'Area do circulo: {area}')
