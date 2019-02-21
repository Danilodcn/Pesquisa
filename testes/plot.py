import numpy as np
import matplotlib.pyplot as plt
from random import sample

N_CIDADES = 10
COOR_CIDADES = [[0, 0]] * N_CIDADES
f = lambda x: x ** 2
for i in range(N_CIDADES):
    k = int(N_CIDADES / 2) - N_CIDADES + i
    COOR_CIDADES[i] = [k, f(k)]

#COOR_CIDADES = sample(COOR_CIDADES, N_CIDADES)

x, y = [], []
lista = list(range(N_CIDADES))
for k in lista:
    i, j = COOR_CIDADES[k]
    x.append(i); y.append(j)

plt.plot( x, y, 'go') # green bolinha
plt.plot( x, y, 'k:', color='orange') # linha pontilha orange

plt.grid(True)
plt.show()
