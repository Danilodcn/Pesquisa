
from Caixeiro.constantes import *
from Caixeiro.funcoes import *
from random import sample

class Individuo:
    def __init__(self, ini = CIDADE_PARTIDA, n = N_CIDADES):
        self.cromossomo = []
        self.n = n
        self.partida = ini

    def __len__(self): return len(self.cromossomo)

    def __repr__(self): return "Individuo: {}".format(self.cromossomo)

    def getGene(self, i): return self.cromossomo[i]

    def setGene(self, o, i): self.cromossomo[i] = o

    def getCromossomo(self): return self.cromossomo

    def setCromossomo(self, o): self.cromossomo = list(o).copy()

    def getGenes(self, i, j): return self.cromossomo[i:j]

    def geraCromossomo(self):
        l = []
        for i in range(self.n):
            if i != self.partida: l.append(i)
        self.cromossomo = [self.partida] + l + [self.partida]
        self.n -= 1

    def permutacao(self):
        l = sample(self.getGenes(1, self.n+1), self.n)
        self.cromossomo = [self.partida] + l + [self.partida]



















if __name__ == "__main__":
    i = Individuo()
    i.geraCromossomo()
    print(i)
    i.permutacao()
    print(i.getGenes(0, 2), i)



