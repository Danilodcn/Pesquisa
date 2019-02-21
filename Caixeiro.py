from math import sqrt
from random import sample, getrandbits

#   Parametros Usados
N_CIDADES = 10                      #Numero de Cidades
COR_CIDADES = [[0, 0]] * N_CIDADES    #Cordenadas das cidades

for i in range(N_CIDADES):
    k = int(N_CIDADES / 2) - N_CIDADES + i
    COR_CIDADES[i] = [k, abs(k)]

print(COR_CIDADES)


class Cidade:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

    def __eq__(self, other):
        condicoes = [self.x == other.x, self.y == other.y]
        return True if all(condicoes) else False

    def __repr__(self): return "Cidade: ({}, {})".format(self.getX(), self.getY())

    def getX(self): return self.x

    def getY(self): return self.y

    def getCordenadas(self): return self

    def distancia(self, o):
        dx = self.x - o.x; dy = self.y - o.y
        return sqrt(dx ** 2 + dy ** 2)

    def modulo(self): return self.distancia(Cidade(0, 0))


class Individuo:
    def __init__(self):
        self.cromossomo = [None] * N_CIDADES
        self.carregaCidades()

    def __str__(self): return "Individuo: {}".format(self.getCromossomo())

    def __len__(self): return len(self.cromossomo)

    def carregaCidades(self, cordenadas = COR_CIDADES):
        for i, j in enumerate(cordenadas): self.cromossomo[i] = Cidade(j[0], j[1])

    def getCromossomo(self): return self.cromossomo

    def getGene(self, i): return self.cromossomo[i]

    def setGene(self, gene, i): self.cromossomo[i] = gene

    def objetivo(self):
        dis = 0
        for i in range(0, self.__len__() - 1):
            c1, c2 = self.getCromossomo()[i:i+2]
            dis += c1.distancia(c2)
        return dis

    def aptidao(self): return self.objetivo()

    def crossoverUniforme(self, o):
        b = getrandbits(self.__len__())
        b = bin(b)[2:]
        print(b)
        l = []
        f0 = Individuo()
        for i, c in enumerate(b):
            if c == "1": f0.setGene(self.cromossomo[i], i)
            elif c == "0": l += self.cromossomo[i]

        print(f0, b)

i = Individuo()
i2 = Individuo()
i2.cromossomo.reverse()

i.crossoverUniforme(i2)