"""
04.252.011/0001-10
40.688.134/0001-61
71.506.168/0001-11
12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1   X   X
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segundo digito
"""
from random import randint

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def formatar(cnpj):
    return str(cnpj).replace('.', '').replace('/', '').replace('-', '').replace(' ', '')


def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    else:
        return False


def calcular_digito(cnpj, digito):
    cnpj = formatar(cnpj)
    if digito == 1:
        multiplicadores = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        multiplicadores = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    for indice, multiplicador in enumerate(multiplicadores):
        total += int(cnpj[indice]) * multiplicador

    digito = 11 - (total % 11)
    if digito < 9:
        novo_cnpj += str(digito)
    else:
        novo_cnpj += '0'

    return novo_cnpj


def validar(cnpj):
    cnpj = formatar(cnpj)

    if eh_sequencia(cnpj):
        return False

    novo_cnpj = calcular_digito(cnpj=cnpj, digito=1)
    novo_cnpj = calcular_digito(cnpj=novo_cnpj, digito=2)

    if novo_cnpj == cnpj:
        return True
    else:
        return False


def gerar():
    primeiro_bloco = str(randint(0, 9)) + str(randint(0, 9))
    segundo_bloco = str(randint(100, 999))
    terceiro_bloco = str(randint(100, 999))
    quarto_bloco = '0001'
    cnpj = f'{primeiro_bloco}.{segundo_bloco}.{terceiro_bloco}/{quarto_bloco}-00'

    cnpj_com_d1_calculado = calcular_digito(cnpj=cnpj, digito=1)
    cnpj_com_d2_calculado = calcular_digito(cnpj=cnpj_com_d1_calculado, digito=2)

    novo_cnpj = f'{cnpj[:-2]}{cnpj_com_d2_calculado[-2:]}'
    return novo_cnpj


if __name__ == '__main__':
    print(gerar())
