import numpy as np
import matplotlib.pyplot as plt
import math

i = complex(0, 1)


def Angular(l, m, theta):
    ANG = []
    if l == 1:
        ANG = [(math.sqrt(3 / (4 * np.pi)) * np.cos(angle)) ** 2 for angle in theta]
    elif l == 2:
        if m == 0:
            ANG = [(math.sqrt(5 / (16 * np.pi)) * (1 - 3 * np.cos(angle) * np.cos(angle))) ** 2 for angle in theta]
        elif m == 1:
            ANG = [(-math.sqrt(15 / (8 * np.pi)) * np.cos(angle) * np.sin(angle) * math.exp(angle * i)) ** 2 for angle
                   in theta]
    elif l == 3:
        if m == 0:
            ANG = [(-math.sqrt(7 / (16 * np.pi)) * np.cos(angle) * (5 * np.cos(angle) * np.cos(angle) - 3)) ** 2 for
                   angle in theta]
        elif m == 1:
            ANG = [(- math.sqrt(21 / (64 * np.pi)) * np.sin(angle) * (5 * np.cos(angle) * np.cos(angle) - 1) * math.exp(
                angle * i)) ** 2 for angle in theta]
        elif m == 2:
            ANG = [(-math.sqrt(105 / (32 * np.pi)) * np.cos(angle) * np.sin(angle) * np.sin(angle) * np.sin(
                angle) * np.sin(angle) * math.exp(2 * angle * i)) ** 2 for angle in theta]
    return ANG
