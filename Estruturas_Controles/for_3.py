produto = {'nome': 'Caneta Chique', 'preco': 14.99,
           'importado': True, 'estoque': 793}

for chave in produto:
    print(chave)
print()
# Ou para acessa o valor da chave utilizar "KEYS"
for chave1 in produto.keys():
    print(chave1)
print()
for valor in produto.values():
    print(valor)
print()
for chave, valor in produto.items():
    print(chave, '=', valor)
print()
print(f'{chave} = {valor}')
