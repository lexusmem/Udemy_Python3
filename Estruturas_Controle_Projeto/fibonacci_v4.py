# Sequência fibonacci
# 0, 1, 1, 2, 3, 5, 8, ...


def fibonacci(limite):
    # Criar Lista:
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(int(input('Informe o numero de numero: '))):
        print(fib)
