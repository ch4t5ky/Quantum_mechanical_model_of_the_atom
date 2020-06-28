import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
import math
from Wave_functions.Radial import *
from Wave_functions.Angular import *

def WAVE(R, PHI, THETA):
    Rad = Radial(3, 2, R)
    Ang = Angular(2, 1, THETA)
    RES = []
    for i in range(len(Rad)):
        RES.append(Rad[i] * Ang[i])
    return RES

radius, theta, phi = [], [], []
X, Y, Z =[], [], []
for r in np.arange(0, 5, 0.5):
    for t in np.arange(0, 2*math.pi, 0.5):
        for ph in np.arange(0, 2*math.pi, 0.5):
            radius.append(r)
            theta.append(t)
            phi.append(ph)
            Z.append(r*math.sin(t)*math.cos(ph))
            Y.append(r*math.sin(t)*math.sin(ph))
            X.append(r*math.cos(t))
ALPHA = WAVE(radius, phi, theta)

Max_ver = max(ALPHA)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
for i in range(0, len(Z)):
    ax.scatter([X[i]], [Y[i]], [Z[i]], c="red", alpha=(abs(ALPHA[i]/Max_ver)))
plt.ylabel("θ")
ax.set_zlabel("φ")
plt.show()


