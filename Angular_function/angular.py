import numpy as np
import matplotlib.pyplot as plt
import math
import cmath

plt.subplot(111, polar=True)

i = complex(0, 1)

phi = np.arange(0, 2*np.pi, 0.001)

# L=1 M=0
# rho = [(math.sqrt(3/(4*np.pi)) * np.cos(angle) ) ** 2 for angle in phi]

# L=2 M=0
# rho = [(math.sqrt(5/(16*np.pi))*(1-3*np.cos(angle)*np.cos(angle)))**2 for angle in phi]

# L=2 M=1
#rho = [(-math.sqrt(15/(8 * np.pi)) * np.cos(angle) * np.sin(angle) * math.exp(angle * i)) ** 2 for angle in phi]

# L=3 M=0
# rho = [(-math.sqrt(7/(16*np.pi)) * np.cos(angle) * (5 * np.cos(angle)*np.cos(angle) - 3)) ** 2 for angle in phi]

# L=3 M=1
# rho = [(- math.sqrt(21/(64*np.pi)) * np.sin(angle) * (5*np.cos(angle)*np.cos(angle) - 1) * math.exp(angle * i)) ** 2 for angle in phi]

# L=3 M=2
rho = [(-math.sqrt(105/(32*np.pi)) * np.cos(angle) * np.sin(angle) * np.sin(angle) * np.sin(angle) * np.sin(angle) * math.exp(2 * angle * i) ) ** 2 for angle in phi]


plt.plot(phi, rho, lw=2)
plt.show()

