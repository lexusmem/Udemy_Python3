from string import Template
nome, idade = 'Alex', (2021-1987)

# Primeira Opção para interpolação de dados
print('Nome: %s Idade: %d' % (nome, idade))# Versão mais antiga
# %s -> String
# %d -> Inteiro
numero_float = 31.5555
print('Numero com casas decimais: %f' % (numero_float))# Versão mais antiga
# %f -> Float (ponto flutuante)
print('Numero com casas decimais arrendodado: %.2f' % (numero_float))# Versão mais antiga
# %.2f -> Float com Arredondamento(ponto flutuante)

# Segunda Opção para interpolação de dados
print('Nome: {0} Idade: {1}'.format(nome,idade)) #Opção mais recomendada para python <3.6
# Terceira Opção para interpolação de dados
print(f'Nome: {nome} Idade: {idade} Posso inserir dados direto: {1 + 2}->Teste')#Opção mais recomendada python atual >=3.6

s = Template ('Nome: $nome_template Idade: $idade_template')
print(s.substitute(nome_template=nome, idade_template=idade))