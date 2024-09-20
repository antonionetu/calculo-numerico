PRECISAO = 10 ** (-3)


def ponto_medio(a, b):
    return (a+b)/2


def modulo(num):
    if num < 0:
        return num * -1
    return num


def bolzano(FUNCAO, a, b):
    return FUNCAO(a) * FUNCAO(b) < 0


def metodo(FUNCAO, a, b):
    pm = ponto_medio(a, b)
    if modulo(FUNCAO(pm)) <= PRECISAO:
        return pm

    if bolzano(FUNCAO, a, pm):
        return metodo(FUNCAO, a, pm)
    return metodo(FUNCAO, pm, b)
