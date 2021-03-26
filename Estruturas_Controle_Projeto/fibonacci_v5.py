# Sequência fibonacci
# 0, 1, 1, 2, 3, 5, 8, ...


def fibonacci(limite):
    # Criar Lista:
    resultado = [0, 1]
    while resultado[-1] < limite:
        # Função Sum [-2:] soma do 2 ultimo elementos.
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(int(input('Informe o numero de numero: '))):
        print(fib)
