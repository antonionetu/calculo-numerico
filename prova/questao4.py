from handle import Bisseccao

G = 9.8
M = 110
V = 40
T = 7
E = 2.7
PRECISAO = 10 ** (-6)


def FUNCAO(c):
    c = c if c != 0 else PRECISAO

    return (
        (G * M * (1 - E**(-T*(c/M))))
        /
        c
    ) - V


bisseccao = Bisseccao(
    funcao=FUNCAO,
    precisao=PRECISAO
)

print(bisseccao.metodo(10, 20))
