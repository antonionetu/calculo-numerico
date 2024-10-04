from handle import Bisseccao

PRECISAO = 10 ** (-10)


def FUNCAO(x):
    return 2*x - x**2


bisseccao = Bisseccao(
    funcao = FUNCAO,
    precisao = PRECISAO
)

print(bisseccao.metodo(1, 10))
