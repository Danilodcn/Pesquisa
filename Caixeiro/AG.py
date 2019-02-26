from Caixeiro.Populacao import Populacao
from Caixeiro.constantes import *

class AG:
    def __init__(self):
        self.n = 0
        self.populacao = Populacao()
        self.populacao.geraAleatoriamente()
        self.mudouMenor = 0

    def menor(self): return self.populacao.menor()

    def proximaGeracao(self):
        self.n += 1
        for i in range(N_CROSSOVER):
            x = self.populacao.selecaoTorneio()
            y = self.populacao.selecaoTorneio()
            f = x.crossover(y)
            self.populacao.add(f)

