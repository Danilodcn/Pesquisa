
from Caixeiro.constantes import *
from Caixeiro.funcoes import *
from random import sample

class Individuo:
    def __init__(self, ini = CIDADE_PARTIDA, n = N_CIDADES):
        self.cromossomo = []
        self.n = n - 1
        self.partida = ini
        self.geraCromossomo()

    def __len__(self): return len(self.cromossomo)

    def __repr__(self): return "Individuo: {}".format(self.cromossomo)

    def getGene(self, i): return self.cromossomo[i]

    def setGene(self, o, i): self.cromossomo[i] = o

    def getCromossomo(self): return self.cromossomo

    def setCromossomo(self, o): self.cromossomo = list(o).copy()

    def getGenes(self, i, j): return self.cromossomo[i:j]

    def geraCromossomo(self):
        l = []
        for i in range(self.n+1):
            if i != self.partida: l.append(i)
        self.cromossomo = [self.partida] + l + [self.partida]

    def permutacao(self):
        l = sample(self.getGenes(1, self.n+1), len(self)-2)
        self.cromossomo = [self.partida] + l + [self.partida]

    def copy(self):
        f = Individuo(self.partida, self.n)
        f.setCromossomo(self.cromossomo)

    def objetivo(self): return distanciaTotal(COORDENADAS, self.getCromossomo())

    def aptidao(self): return self.objetivo()



















if __name__ == "__main__":
    COORDENADAS = [[-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
    print(COORDENADAS)
    i = Individuo()
    print(i, i.objetivo())
    i.permutacao()
    print(i.getGenes(0, 2), i, i.objetivo())



