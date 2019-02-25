import random
from time import time



#   Parametros Usados
N_CIDADES = 10                      #Numero de Cidades
COOR_CIDADES = [[0, 0]] * N_CIDADES    #Cordenadas das cidades
CIDADE_DE_PARTIDA = 0
TAM_POPULACAO = 1000
MAX_GERACAO = 100
N_CRIAR = 20
TAXA = 1                           #taxa de mutacao
DIC = {"mudaOrdem": int(TAM_POPULACAO * 0.01),
       "mistura": int(TAM_POPULACAO * 0.2),
       "inversao": int(TAM_POPULACAO * 0.2)}
DIC["permutacao"] = TAM_POPULACAO - sum(DIC.values())

print(DIC.values())

f = lambda x: random.randint(-10000, 10000)
for i in range(N_CIDADES):
    k = int(N_CIDADES / 2) - N_CIDADES + i
    COOR_CIDADES[i] = [k * 100, f(k)]
#COOR_CIDADES = [[-5, 11], [-4, -67], [-3, -38], [-2, -96], [-1, 36], [0, -74], [1, 29], [2, 98], [3, 49], [4, -23]]
print(COOR_CIDADES)


distancia = lambda x1, y1, x2, y2: ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def somaDistancias(lista = None):
    if lista == None: lista = list(range(N_CIDADES))
    soma = 0
    for i in range(len(lista)):
        if i == len(lista) - 1: break#i = - 1
        m, n = lista[i], lista[i+1]
        x, y = COOR_CIDADES[m]; z, w = COOR_CIDADES[n]
        soma += distancia(x, y, z, w)
    return soma


def insertionSort(args):
    args = list(args)
    for j in range(1, len(args)):
        x = args[j]
        i = j - 1
        while i >= 0 and args[i].aptidao() < x.aptidao():
            args[i+1] = args[i]
            i = i - 1
        args[i+1] = x
    return args

def mostraPopulacao(p):
    print("\t\t\tPOPULACAO ORDENADA\n")
    print("n\t\t\tCromossomo\t\t\t\t\tAptidao\n")
    for i in range(int(len(p) * 0), int(len(p) * 0.1)):
        a = p.getMembro(i)
        print("{}\t{}\t{}".format(i, a.cromossomo, a.aptidao()))
    for i in range(int(len(p) * 0.9), len(p)):
        a = p.getMembro(i)
        print("{}\t{}\t{}".format(i, a.cromossomo, a.aptidao()))


class Individuo:
    def __init__(self):
        self.cromossomo = []
        self.geraIndividuo()
        self.permutacao()

    def __eq__(self, other): return self.cromossomo == other.cromossomo

    def __str__(self): return "Idividuo: {} {}".format(self.cromossomo, self.aptidao())

    def __repr__(self): return str(self)

    def __len__(self): return len(self.getCromossomo())

    def geraIndividuo(self):
        l = list(range(N_CIDADES))
        a = l[0:CIDADE_DE_PARTIDA]; b = l[CIDADE_DE_PARTIDA+1:]
        self.cromossomo = [CIDADE_DE_PARTIDA] + a + b

    def getCromossomo(self): return self.cromossomo

    def setCromossomo(self, cro): self.cromossomo = cro.copy()

    def getGene(self, i): return self.cromossomo[i]

    def setGene(self, gene, i): self.cromossomo[i] = gene

    def copy(self):
        filho = Individuo()
        filho.setCromossomo(self.getCromossomo())
        return filho

    def objetivo(self): return somaDistancias(self.getCromossomo())

    def aptidao(self): return self.objetivo()

    def permutacao(self):
        cro = [CIDADE_DE_PARTIDA] + random.sample(self.getCromossomo()[1:], len(self)-1)
        self.setCromossomo(cro)

    def crossoverUniforme(self, o):
        f1 = Individuo(); f2 = Individuo()
        b = bin(random.getrandbits(len(self)))[2:]
        b = "0" * (len(self) - len(b)) + b
        l1, l2 = [], []; ordem1, ordem2 = [], []
        for i in range(len(self)):
            if b[i] == "1":
                f1.setGene(self.getGene(i), i)
                l2.append(o.getGene(i))
            elif b[i] == "0":
                l1.append(self.getGene(i))
                f2.setGene(o.getGene(i), i)
        for i in range(len(self)):
            if o.getGene(i) in l1: ordem1.append(o.getGene(i))
            if self.getGene(i) in l2: ordem2.append(self.getGene(i))
        k, m = 0, 0
        for i in range(len(self)):
            if b[i] == "0":
                f1.setGene(ordem1[k], i)
                k = k + 1
            else:
                f2.setGene(ordem2[m], i)
                m = m + 1
        r = insertionSort((f1, f2, self))
        return r[-1]

    def mutacaoPermutacaoElementos(self, taxa=TAXA):
        i = random.random()
        filho = self.copy()
        if i <= taxa:
            k = random.randrange(1, len(self))
            for u in range(k):
                i, j = random.sample(range(len(self)), 2)
                x, y = filho.getGene(i), filho.getGene(j)
                filho.setGene(x, j); filho.setGene(y, i)

        #r = insertionSort((self, filho))
        return filho#r[-1]

    def mutacaoPermutacao(self):
        filho = self.copy()
        filho.permutacao()
        #r = insertionSort((self, filho))
        return filho #r[-1]

    def mutacaoMistura(self, taxa=TAXA):
        filho = self.copy()
        if taxa >= random.random():
            seq = random.sample(self.getCromossomo(), 2)
            seq.sort(); i, j = seq
            a = self.cromossomo[:i]
            b = self.cromossomo[j:]
            c = self.cromossomo[i:j]
            c = random.sample(c, len(c))
            seq = a + c + b
            filho.setCromossomo(seq)
        #r = insertionSort((self, filho))
        return filho#r[-1]

    def mutacaoInversao(self, taxa=TAXA):
        filho = self.copy()
        if taxa >= random.random():
            seq = random.sample(self.getCromossomo(), 2)
            seq.sort();i, j = seq
            if i - j <= 1 and j < len(self): j = j + 1
            a = self.cromossomo[:i]
            b = self.cromossomo[j:]
            c = self.cromossomo[i:j]
            c.reverse()
            seq = a + c + b
            filho.setCromossomo(seq)
        #r = insertionSort((self, filho))
        return filho#r[-1]


class Populacao:
    def __init__(self):
        self.membros = []

    def __len__(self): return len(self.membros)

    def __repr__(self): str(self)

    def __str__(self): return "Populacao: {}".format(self.getMebros())

    def getMebros(self): return self.membros

    def setMembros(self, lista): self.membros = lista.copy()

    def getMembro(self, i): return self.membros[i]

    def setMembro(self, individuo, i): self.membros[i] = individuo

    def geraPopulacao(self):
        x = [Individuo() for i in range(TAM_POPULACAO)]
        self.setMembros(x)

    def selecaoTorneio(self, n = 2):
        seq = [random.choice(self.getMebros()) for i in range(n)]
        r = insertionSort(seq)
        return r[-1]

    def menor(self):
        m = self.getMembro(0)
        for i in range(1, len(self)):
            x = self.getMembro(i)
            if x.aptidao() < m.aptidao(): m = x
        return m

    def ordena(self):
        l = self.getMebros()
        o = insertionSort(l)
        self.setMembros(o)


class AG:
    def __init__(self):
        self.geracao = 1
        self.populacao = Populacao()
        self.populacao.geraPopulacao()
        self.min = self.menor()
        self.mudancaMenor = 0

        while self.geracao <= MAX_GERACAO and self.mudancaMenor <= 10:
            self.min = self.menor()
            self.proximaGeracao()
            self.min = self.menor()
            self.mutacao()
            self.min = self.menor()
            print(self.min, self.geracao, self.mudancaMenor)


    def proximaGeracao(self):
        self.geracao += 1
        p = Populacao(); t = []
        for i in range(len(self.populacao)-N_CRIAR):
            x = self.populacao.selecaoTorneio()
            y = self.populacao.selecaoTorneio()
            r = x.crossoverUniforme(y)
            t.append(r)
        p.membros = t.copy()
        x, y = self.menor(), p.menor()
        p.membros += [Individuo() for i in range(N_CRIAR)]
        if x.aptidao() == y.aptidao(): self.mudancaMenor += 1
        elif x.aptidao() > y.aptidao():
            self.mudancaMenor = 0
            self.populacao.membros[0] = y
        elif x.aptidao() < y.aptidao():
            self.mudancaMenor = 0
            p.membros[0] = x

        self.populacao.membros = p.membros.copy()


    def menor(self): return self.populacao.menor()

    def mutacao(self):
        per, mis, inv,  muda= DIC["permutacao"], DIC["mistura"], DIC["mudaOrdem"], DIC["inversao"]
        for i in range(1, per): self.populacao.membros[i].mutacaoPermutacaoElementos()
        for i in range(per, per + mis): self.populacao.membros[i].mutacaoMistura()
        for i in range(per + mis, per + mis + inv): self.populacao.membros[i].mutacaoInversao()
        for i in range(per + mis + inv, TAM_POPULACAO): self.populacao.membros[i].mutacaoPermutacao()


t = time()

a = AG()
a.populacao.ordena()
mostraPopulacao(a.populacao)
print(a.menor(), a.geracao, a.mudancaMenor)

print("Tempo gasto: {}".format(time() - t))

import matplotlib.pyplot as plt

x, y = [], []
lista = a.menor().cromossomo
for k in lista:
    i, j = COOR_CIDADES[k]
    x.append(i); y.append(j)

plt.plot( x, y, 'go') # green bolinha
plt.plot( x, y, 'k:', color='orange') # linha pontilha orange

plt.grid(True)
plt.show()