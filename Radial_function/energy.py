import numpy as np

E_0 = 27.07 * 1.6 / (10 ** 19)
n = [1, 2, 3, 4]
E = [0] * 4
electron=-1.6 / (10 ** 19)
epsilon_0= 8.85/(10 ** 12)
a=5.29/(10 ** 11)

def findEi(i):
    return -(electron ** 2)/(8 * np.pi * a * epsilon_0 * n[i] ** 2)

for i in range(0, len(n)):
    E[i] = findEi(i)
    print(float('{:.3f}'.format(E[i]/ (1.6*10**(-19)))))

