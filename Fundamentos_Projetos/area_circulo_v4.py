#! python
# Shibang - Indicação do interpretador que será utilizado p executar o script

import math
# Modulo "math"
# Módulo especifico para operações matematicas
# E algumas constantes, como por exemplo PI

from math import pi
# Forma para importar apenas o PI do modulo Math


print('Funcoes disponiveis no modulo Math:\n', dir(math))
print(f'Valor de Pi = {pi}')
print('Valor de Pi (4 casas decimais)= %.4f' % (pi))
raio = 15.3
area = pi * raio**2
print(f'Area do circulo: {area}')
