from math import *

#Константы
epsilon = 1000


def Radial_nl(p):
    result = 0
    return result


def A_nl(n, l):
    part1 = 1 / factorial(2 * l + 1)
    part2 = sqrt(factorial(n + l) / (2 * n * factorial(n - l - 1)))
    beta = sqrt(2*epsilon)
    z=n*beta
    part3 = ((2 * z) / n) ** (3 / 2)
    result = part1 * part2 * part3
    return result

def L_alpha_gamma(alpha, gamma, ksi):
    result=0

quantum_numbers = [1, 2, 3, 4]
