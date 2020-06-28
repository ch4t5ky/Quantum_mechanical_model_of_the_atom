from math import *
import numpy as np
a = 0.529


def Radial(n, l, R):
    RAD = []
    if n == 1:
        for i in R:
            RAD.append(2 / (a ** (3 / 2)) * np.exp(-i / a))
    elif n == 2:
        if l == 0:
            for i in R[0]:
                RAD.append((1 / sqrt(2 * a ** 3) * (1 - (i / (2 * a))) * np.exp(-i / (2 * a))))
        elif l == 1:
            for i in R:
                print(i)
                RAD.append((1 / sqrt(6 * a ** 3) * (i / a) * np.exp(-i / (2 * a))))
    elif n == 3:
        if l == 0:
            for i in R:
                RAD.append((2 / (3 * sqrt(3 * a ** 3)) * (
                            1 - (2 * i / (3 * a)) + (2 * (i ** 2) / (27 * (a ** 2)))) * np.exp(-i / (3 * a))))
        elif l == 1:
            for i in R:
                RAD.append((8 / (27 * sqrt(6 * a ** 3)) * (i / a) * (1 - (i / (6 * a))) * np.exp(-i / (3 * a))))
        elif l == 2:
            for i in R:
                RAD.append((4 / (81 * sqrt(30 * a ** 3)) * ((i ** 2) / (a ** 2)) * np.exp(-i / (3 * a))))
    return RAD
