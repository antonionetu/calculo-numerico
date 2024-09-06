TERACOES = 0

def ponto_medio(a, b):
    return (a+b)/2


def modulo(num):
    if num < 0:
        return num * -1
    return num


def bolzano(a, b):
    return FUNCAO(a) * FUNCAO(b) < 0


def bisseccao(a, b):
    pm = ponto_medio(a, b)
    ITERACOES += 1

    if modulo(FUNCAO(pm)) <= PRECISAO:
        return pm

    if bolzano(a, pm):
        return bisseccao(a, pm)
    return bisseccao(pm, b)


# Constantes
EULER = 2.71

# Precisao
PRECISAO = 10 ** (-9)

# Funcao
def FUNCAO(x):
    return 2 * x * (EULER**x) -3


# Resultado
print(bisseccao(-10000, 10000))
print(ITERACOES)
