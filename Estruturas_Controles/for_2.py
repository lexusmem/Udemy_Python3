palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end=',')
print('Fim!')

aprovados = ['Alex', 'Rafaela', 'Pedro', 'Maria']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1}) {nome}')

dias_semana = ('Domingo', 'Segunda', 'Terca',
               'Quarta', 'Quinta', 'Sexta', 'Sabado')
for dias in dias_semana:
    print(f'Hoje e {dias}!')

for letra in set('Muito Legal!'):
    print(letra)

print('\n')

for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
