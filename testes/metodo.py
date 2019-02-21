from math import sin, pi, exp


df = lambda x, y: exp(-40* x) * (sin(x))

X, Y = [], []
def euler(xn, x, y, h = 0.01):
    x1 = x + h
    y1 = y + df(x, y) * h
    X.append(x1); Y.append(y1)
    if abs(xn-x1) <= h: return x1, y1
    else: return euler(xn, x1, y1, h)


from matplotlib import pyplot as plt

def plotar(x, y):

    plt.plot(x, y, 'go') # green bolinha
    plt.plot(x, y, 'k:', color='orange') # linha pontilha orange

    plt.grid(True)
    plt.show()

s = euler(2.5, 0, 0, 0.01)
print(s)
plotar(X, Y)
X, Y = [], []
s = euler(10, 2.5, 1.9533)
print(s)
plotar(X, Y)
X, Y = [], []