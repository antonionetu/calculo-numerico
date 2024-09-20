PRECISAO = 10 ** (-3)

def MODULO(n):
    if n < 0:
        return n * -1
    return n


def formula(FUNCAO, DERIVADA_FUNCAO, x):
    return x - (FUNCAO(x)/DERIVADA_FUNCAO(x))


def metodo(FUNCAO, DERIVADA_FUNCAO, CHUTE):
    if MODULO(FUNCAO(CHUTE)) < PRECISAO:
        return CHUTE

    return metodo(FUNCAO, formula(FUNCAO, DERIVADA_FUNCAO, CHUTE))
