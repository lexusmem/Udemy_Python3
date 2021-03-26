""" for i in range(1, 11):
    if i == 6:
        break
    print(i)
else:
    print('Fim!')
print() """

# criar função(sortear_dado) jogar dado entre 1 e 6
# criar for para percorrer de range 1 a 6
# excluir numeros impares (continue)
# se numero for par e for == ao valor sorteado pela função dado
# imprimir a string 'acertou' e depois chamar o break
# se não achar chama o else (o numero não acertado)

from random import randint


def sortear_dado():
    return randint(1, 6)


valor = sortear_dado()

for x in range(1, 7):
    if x % 2 != 0:
        continue

    if x == valor:
        print(f'Valor do Sorteado = {valor}')
        print(f'Valor do X = {x}')
        print('Acertou!')
        break
else:
    print(f'Valor do Sorteado = {valor}')
    print(f'Valor do X = {x}')
    print('Nao acertou!')
