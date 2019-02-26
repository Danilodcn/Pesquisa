from math import hypot, exp

distancia = lambda p1, p2: hypot((p1[0] - p2[0]), (p1[1] - p2[1]))
f = lambda x: exp(x)

def distanciaTotal(coor, seq):
    s = 0
    for i in range(len(seq)):
        if i == len(seq) - 1: break
        j, k = seq[i], seq[i+1]
        s += distancia(coor[j], coor[k])
    return s

def geraCoordenadas(n):
    coor = [(0, 0)] * n
    for i in range(n):
        k = int(n / 2) - n + i
        coor[k] = [k, f(k)]
    return coor

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
