try:
    from Caixeiro.Populacao import Populacao
    from Caixeiro.constantes import *
    from Caixeiro.funcoes import plotar
except:
    from Populacao import Populacao
    from constantes import *
    from funcoes import plotar

from random import sample
from time import time

class AG:
    def __init__(self):
        self.n = 0
        self.populacao = Populacao()
        self.populacao.geraAleatoriamente()
        self.minimo = self.menor()
        self.mudouMenor = 0
        self.duracao = 0
        print(self.minimo, self.n, self.mudouMenor)
        t0 = time()
        while self.n <= 100 and self.mudouMenor < MUDANCA_MENOR:
            self.proximaGeracao()
            t1 = time()
            self.duracao += t1 - t0
            print(self.minimo, self.n, self.mudouMenor, t1 - t0)
            t0 = t1

    def menor(self): return self.populacao.menor()

    def proximaGeracao(self):
        self.n += 1
        m = self.minimo.copy()
        for i in range(N_CROSSOVER):
            x = self.populacao.selecaoTorneio()
            y = self.populacao.selecaoTorneio()
            f = x.crossover(y)
            self.populacao.add(f)
            if self.minimo.aptidao() > f.aptidao(): self.minimo = f.copy()

        for i in range(N_MUTACAO):
            x = self.populacao.selecaoTorneio()
            f = x.mutacao()
            self.populacao.add(f)
            if self.minimo.aptidao() > f.aptidao(): self.minimo = f.copy()

        seq = sample(self.populacao.membros, TAM_POPULACAO)
        self.populacao.membros = seq.copy()

        if m.aptidao() == self.minimo.aptidao(): self.mudouMenor += 1
        else: self.mudouMenor = 0



if __name__ == "__main__":
    g = AG()
    print(g.minimo, "Duracao: {}".format(g.duracao))
    g.populacao.ordena()
    g.populacao.mostraPopulacao()
    plotar(g.minimo.cromossomo, COORDENADAS)
