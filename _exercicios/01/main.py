from bisseccao.operacoes import metodo as bisseccao

A = 8500
P = 35000
n = 7


def FUNCAO(i):
    u = (i+1)**n

    return P * (
        (i * u)
        /
        (u - 1)
    ) - A


minimo = 10 ** (-3)
print(bisseccao(FUNCAO, minimo, 1.0))
