from handle import Newton
from math import cos, sin


PRECISAO = 10 ** (-5)


def FUNCAO(x):
    return x * cos(x) + 4


def DERIVADA_FUNCAO(x):
    return -x * sin(x) + cos(x)


newton = Newton(
    funcao=FUNCAO,
    derivada_funcao=DERIVADA_FUNCAO,
    precisao=PRECISAO
)

print(newton.metodo(8))
print(newton.metodo(10))
