from Caixeiro.Individuo import Individuo
from Caixeiro.constantes import TAM_POPULACAO as TAM
from random import sample
from Caixeiro.funcoes import insertionSort as ordenar, mostraPopulacao

class Populacao:
    def __init__(self, tam = TAM):
        self.membros = [Individuo() for i in range(tam)]
        self.geraAleatoriamente()

    def __len__(self): return len(self.membros)

    def __repr__(self): return "Populacao: {}".format(self.menor())

    def getMembro(self, i): return self.membros[i]

    def setMembro(self, o, i): self.membros[i] = o

    def setMembros(self, lista): self.membros = lista.copy()

    def menor(self):
        m = self.getMembro(0)
        for i in range(1, len(self)):
            x = self.getMembro(i)
            if x.aptidao() < m.aptidao(): m = x
        return m

    def geraAleatoriamente(self):
        for i in range(len(self)): self.membros[i].permutacao()

    def selecaoTorneio(self, n=2):
        seq = sample(self.membros, n)
        r = ordenar(seq)
        return r[-1]

    def ordena(self): self.membros = ordenar(self.membros)

    def mostraPopulacao(self): mostraPopulacao(self)







if __name__ == "__main__":
    p = Populacao()
    print(p)
    p.ordena()
    p.mostraPopulacao()
