def MODULO(n):
    if n < 0:
        return n * -1
    return n


def formula(x):
    return x - (FUNCAO(x)/DERIVADA_FUNCAO(x))


def newton(x):
    if MODULO(FUNCAO(x)) < PRECISAO:
        return x

    return newton(formula(x))
    


# Precisao
PRECISAO = 10 ** (-3)

# Chute
CHUTE = 5

# Funcao
def FUNCAO(x):
    return 2 * x - x ** 2

# Derivada da funcao
def DERIVADA_FUNCAO(x):
    return 2 - (2 * x)


print(newton(CHUTE))

