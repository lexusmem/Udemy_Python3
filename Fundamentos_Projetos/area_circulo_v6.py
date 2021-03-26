#! python
# Shibang - Indicação do interpretador que será utilizado p executar o script

# particionar o programa em varios arquivos diferentes
# podendo trabalhar com importações de
# pacotes e modulos
# ferramentas disponiveis no python

from math import pi
# Forma para importar apenas o PI do modulo Math

print(f'Valor de Pi = {pi}')
print('Valor de Pi (4 casas decimais)= %.4f' % (pi))

raio = input('Informe o Raio: ')

area = pi * float(raio)**2
print(f'Area do circulo: {area}')

# Nome do modulo principal __name__ (__main__) - Modulo Principal.
print('Nome do módulo', __name__)

print('Nome do pacote', __package__)
print(dir())
