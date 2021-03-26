# Sequência fibonacci
# 0, 1, 1, 2, 3, 5, 8, ...

# Def criação de função
def fibonacci(quantidade):
    # Criar Lista:
    resultado = [0, 1]
    while True:
        # Função Sum [-2:] soma do 2 ultimo elementos.
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(int(input('Informe o num de elementos fibonacci: '))):
        print(fib)
