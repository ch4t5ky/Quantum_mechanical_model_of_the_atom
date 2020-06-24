import numpy as np
import matplotlib.pyplot as plt
import math

plt.subplot(111, polar=True)        # Полярная система координат

phi = np.arange(0, 2*np.pi, 0.001)   # угол phi - массив от от 0 до 2*pi с шагом 0.01
rho = [(math.sqrt(5/(16*np.pi))*(1-3*np.cos(phi[i])*np.cos(phi[i])))**2 for i in range(len(phi))]                         # расстояние от центра 2*phi
plt.plot(phi, rho, lw=2)            # график rho(phi), толщина линии (line width) 2
plt.show()
