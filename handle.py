# Constantes
# ...
PRECISAO = 10 ** (-10)

# Funcoes
def FUNCAO(x):
    return (2 * x) - x ** 2


def DERIVADA_FUNCAO(x):
    return 2 - 2 * x


def modulo(num):
    if num < 0:
        return num * -1
    return num


class Newton:
    @staticmethod
    def formula(x):
        return x - (FUNCAO(x) / DERIVADA_FUNCAO(x))

    def metodo(self, CHUTE):
        if modulo(FUNCAO(CHUTE)) < PRECISAO:
            return CHUTE
        return self.metodo(self.formula(CHUTE))


class Bisseccao:
    @staticmethod
    def ponto_medio(a, b):
        return (a + b) / 2

    @staticmethod
    def bolzano(a, b):
        return FUNCAO(a) * FUNCAO(b) < 0

    def metodo(self, a, b):
        pm = self.ponto_medio(a, b)
        if modulo(FUNCAO(pm)) <= PRECISAO:
            return pm

        if self.bolzano(a, pm):
            return self.metodo(a, pm)
        return self.metodo(pm, b)


class Secante:
    @staticmethod
    def formula(a, b):
        return b - FUNCAO(b) * (
            (b - a) 
            / 
            (FUNCAO(b) - FUNCAO(a))
        )

    def metodo(self, a, b):
        if modulo(FUNCAO(b)) < PRECISAO:
            return b
        return self.metodo(b, self.formula(a, b))


bisseccao = Bisseccao()
newton = Newton()
secante = Secante()
