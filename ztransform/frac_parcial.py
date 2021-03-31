################################################################################################################
#
#               DIGITAL CONTROL - EE/UFSCAR
#
#   Author: André Carmona Hernandes
#   Version: 1
#   Last-Update: 07.03.2021
#
#   Info: Function to compare Partial fractions
#
#   These codes are used in DIGITAL CONTROL classes. You may use and study by them, however use with caution!
#
################################################################################################################

from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np


Ts = 0.1
time_final = 4
n_points = round(time_final / Ts) + 1
time = linspace(0, time_final, n_points)

g_cas1 = tf([3, 0], [1, -1.5, 0.5], Ts)
g_cas2 = tf([1, 1], [1, 0.3, 0.02], Ts)
g_cas3 = tf([1, 0], [1, -2.5, 2, -0.5], Ts)
pp = pole(g_cas3)
print(g_cas3)
print(pp)


y_g, t = impulse(g_cas1, time, 0)
offset = 0.2
x_kt = 6 - 6 * (0.5**(1/Ts)) ** time + offset

y_g2, t = impulse(g_cas2, time, 0)
offset = 0.05
k = np.round(time/Ts)
x2_kt = 50*(k == 0) - 90 * (-1)**k * 0.1 ** k + 40 * (-1)**k * 0.2 ** k + offset

y_g3, t = impulse(g_cas3, time, 0)
offset = 1
k = np.round(time/Ts)
x3_kt = 4 * 0.5 ** k + 2*k - 4 + offset


#
# exp1 = 2 ** time
# exp2 = 4*(2 ** time)
#
fig, axs = plt.subplots(1, 3)
axs[0].step(time, y_g, color=(0, 0.6, 0, 0.5), label="tf", linewidth=3.0, where='post')
axs[0].step(time, x_kt, color=(0, 0, 0.6, 0.5), label="eq", linewidth=3.0, where='post')
# axs.stem(time+0.1, exp2, 'bo')
axs[1].step(time, y_g2, color=(0, 0.6, 0, 0.5), label="tf", linewidth=3.0, where='post')
axs[1].step(time, x2_kt, color=(0, 0, 0.6, 0.5), label="eq", linewidth=3.0, where='post')

axs[2].step(time, y_g3, color=(0, 0.6, 0, 0.5), label="ramp", linewidth=3.0, where='post')
axs[2].step(time, x3_kt, color=(0, 0, 0.6, 0.5), label="eq", linewidth=3.0, where='post')

plt.show()
#
