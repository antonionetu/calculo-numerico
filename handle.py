PRECISAO_PADRAO = 10 ** (-3)


def modulo(num):
    if num < 0:
        return num * -1
    return num


class Newton:
    def __init__(this, **kwargs):
        this.funcao = kwargs.get('funcao')
        this.derivada_funcao = kwargs.get('derivada_funcao')
        this.precisao = kwargs.get('precisao', PRECISAO_PADRAO)
        
    def formula(this, x):
        return x - (this.funcao(x) / this.derivada_funcao(x))

    def metodo(this, CHUTE):
        if modulo(this.funcao(CHUTE)) < this.precisao:
            return CHUTE
        return this.metodo(this.formula(CHUTE))


class Bisseccao:
    def __init__(this, **kwargs):
        this.funcao = kwargs.get('funcao')
        this.precisao = kwargs.get('precisao', PRECISAO_PADRAO)

    @staticmethod
    def ponto_medio(a, b):
        return (a + b) / 2

    def bolzano(this, a, b):
        return this.funcao(a) * this.funcao(b) < 0

    def metodo(this, a, b):
        pm = this.ponto_medio(a, b)
        if modulo(this.funcao(pm)) <= this.precisao:
            return pm

        if this.bolzano(a, pm):
            return this.metodo(a, pm)
        return this.metodo(pm, b)


class Secante:
    def __init__(this, **kwargs):
        this.funcao = kwargs.get('funcao')
        this.precisao = kwargs.get('precisao', PRECISAO_PADRAO)

    def formula(this, a, b):
        return b - this.funcao(b) * (
            (b - a) 
            / 
            (this.funcao(b) - this.funcao(a))
        )

    def metodo(this, a, b):
        if modulo(this.funcao(b)) < this.precisao:
            return b
        return this.metodo(b, this.formula(a, b))
