import matplotlib.pyplot as plt
from math import *
import numpy as np

E_0 = 27.07 * 1.6 / (10 ** 19)
a = 0.529
R_H = 10957758.3407
R_y = R_H * 3 * (10 ** 8) * 6.626 / (10 ** 34)
n = [1, 2, 3, 4]
dp = 0.01
fig, ax = plt.subplots(figsize=(5, 5))
E = [0] * 4


def findEi(i):
    return -R_y / (n[i] ** 2)


def findEpsilon(E):
    return -E / E_0


def findBetta(epsilon):
    return sqrt(2 * epsilon)


R = []
r = []

for j in range(1000):
    r.append(j*dp)

# N=1 L=0
for i in r:
    R.append(2/(a ** (3/2)) * exp(-i/a))
ax.plot(r, R, label = "N=1 L=0")

R = []

# N=2 L=0
for i in r:
    R.append((1/sqrt(2*a ** 3) * (1-(i/(2*a))) * exp(-i/(2*a))))
ax.plot(r, R, label = "N=2 L=0")

R = []
# N=2 L=1
for i in r:
    R.append((1/sqrt(6*a ** 3) * (i/a) * exp(-i/(2*a))))
ax.plot(r, R, label = "N=2 L=1")

R = []
# N=3 L=0
for i in r:
    R.append((2/(3*sqrt(3*a ** 3)) * (1-(2*i/(3*a)) + (2*(i**2)/(27*(a**2)))) * exp(-i/(3*a))))
ax.plot(r, R, label = "N=3 L=0")

R = []
# N=3 L=1
for i in r:
    R.append((8/(27*sqrt(6*a ** 3)) * (i/a) * (1-(i/(6*a))) * exp(-i/(3*a))))
ax.plot(r, R, label = "N=3 L=1")

R = []
# N=3 L=2
for i in r:
    R.append((4/(81 * sqrt(30*a ** 3)) * ((i**2)/(a**2)) * exp(-i/(3*a))))
ax.plot(r, R, label = "N=3 L=2")

ax.legend()


plt.grid()
plt.show()
