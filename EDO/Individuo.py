from EDO.constantes import GRAU, INTERVALO
from random import triangular

class Individuo:
    def __init__(self, n=GRAU):
        self.grau = n
        self.cromossomo = []
        self.geraIndividuo()

    def __repr__(self): return "Individuo: {}".format(self.cromossomo)

    def __len__(self): return len(self.cromossomo)

    def geraIndividuo(self):
        i, j = INTERVALO
        self.cromossomo = [triangular(i, j) for k in range(self.grau)]


