
from Caixeiro.constantes import *
from Caixeiro.funcoes import *
from random import sample, choice

class Individuo:
    def __init__(self, ini = CIDADE_PARTIDA, n = N_CIDADES):
        self.cromossomo = []
        self.n = n - 1
        self.partida = ini
        self.geraCromossomo()

    def __len__(self): return len(self.cromossomo) - 1

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
        l = sample(self.getGenes(1, self.n+1), len(self)-1)
        self.cromossomo = [self.partida] + l + [self.partida]

    def copy(self):
        f = Individuo(self.partida, self.n)
        f.setCromossomo(self.cromossomo)

    def objetivo(self): return distanciaTotal(COORDENADAS, self.getCromossomo())

    def aptidao(self): return self.objetivo()

    def crossover(self, other): return self.edgeRecombination(other)

    def edgeRecombination(self, other):
        filho = Individuo(self.partida, len(self))
        p1 = self.getGenes(0, len(self))
        p2 = other.getGenes(0, len(other))
        tam = len(p1)
        adj = [[] for i in range(tam)]
        for i in range(tam):
            j = i + 1 if i < tam-1 else 0
            adj[p1[i]].append(p1[j]) if p1[j] not in adj[p1[i]] else None
            adj[p1[j]].append(p1[i]) if p1[i] not in adj[p1[j]] else None
            adj[p2[i]].append(p2[j]) if p2[j] not in adj[p2[i]] else None
            adj[p2[j]].append(p2[i]) if p2[i] not in adj[p2[j]] else None

        for i in range(len(adj)): adj[i].sort()

        for i in range(tam): print(adj[i])
        cid_corrente = p1[0]; ja_usadas =[]
        while len(ja_usadas) < tam:
            ja_usadas.append(cid_corrente)
            for i in range(len(adj)):
                try: adj[i].remove(cid_corrente)
                except ValueError: None
            #Escolher a proxima cidade
            if len(adj[cid_corrente]) > 0:
                proxima = adj[cid_corrente][0]
                for w in range(1, len(adj[cid_corrente])):
                    m = adj[cid_corrente][w]
                    if len(adj[m]) < len(adj[proxima]): proxima = m

            else:
                proxima = -1
                for i in range(tam):
                    if i not in ja_usadas:
                        proxima = i; break
            cid_corrente = proxima
        filho.setCromossomo(ja_usadas + [self.partida])
        return filho







if __name__ == "__main__":
    COORDENADAS = [[-5, 5], [-4, 4], [-3, 3], [-2, 2], [-1, 1], [0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
    print(COORDENADAS)
    i = Individuo()
    print(i, i.objetivo())
    i.permutacao()
    print(i.getGenes(0, 2), i, i.objetivo())

    print("#" * 100)
    i1 = Individuo(); i2 = Individuo()
    i2.permutacao(); i1.permutacao()
    i3 = i1.crossover(i2)
    print(i1)
    print(i2)
    print(i3)



