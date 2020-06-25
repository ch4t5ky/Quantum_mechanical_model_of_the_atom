import matplotlib.pyplot as plt
from math import *

E_0 = 27.07 * 1.6 / (10 ** 19)
a = 5.29 / (10 ** 11)
R_H = 10957758.3407
R_y = R_H * 3 * (10 ** 8) * 6.626 / (10 ** 34)
n = [1, 2, 3, 4]
dp = 0.01
fig, ax = plt.subplots(figsize=(5, 5))
E = [0] * 4
F = 1


def findEi(i):
    return -R_y / (n[i] ** 2)


def findEpsilon(E):
    return -E / E_0


def findBetta(epsilon):
    return sqrt(2 * epsilon)


for i in range(len(n)):
    R, p = [], []
    pi = 0
    p0 = 0

    E[i] = findEi(i)
    epsilon = findEpsilon(E[i])
    betta = findBetta(epsilon)

    z = n[i] * betta
    l = i + 1
    v = 0
    m = 0
    for k in range(1000):
        F += factorial(v) * (2 * betta * p0) ** (k + 1) / factorial(2 * m + 2) / factorial(k)
        v += 1
        m += 1
        p0 += dp
        for j in range(1300):
            R.append(
                1 / (factorial(2 * i + 1)) * sqrt((factorial(i + 1) / factorial(0) * 2 * (i + 1))) * (2 * betta) ** (
                        3 / 2) * exp(-betta * pi) * (2 * betta * pi) ** l * F)
            p.append(pi)
            pi += dp
        if v == 4:
            break
    ax.plot(p, R)
plt.grid()
plt.show()
