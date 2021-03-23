# def -> definir função.

def semana_final(dia):
    dias = {
        1: 'Domingo -> Fim de Semana',
        2: 'Segunda-Feira -> Semana',
        3: 'Terca-Feira -> Semana',
        4: 'Quarta-Feira -> Semana',
        5: 'Quinta-Feira -> Semana',
        6: 'Sexta-Feira -> Semana',
        7: 'Sabado-Feira -> Fim de Semana',
    }
    return dias.get(dia, '** invalida **')


if __name__ == '__main__':
    for i in range(0, 9):
        print(f'{i} -> {semana_final(i)}')
