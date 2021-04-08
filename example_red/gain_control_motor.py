################################################################################################################
#
#               DIGITAL CONTROL - EE/UFSCAR
#
#   Author: André Carmona Hernandes
#   Version: 1
#   Last-Update: 08.04.2021
#
#   Info: First Controller
#
#   These codes are used in DIGITAL CONTROL classes. You may use and study by them, however use with caution!
#
################################################################################################################

from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

Ts = 0.02
tfinal = 5
tempo = linspace(0, tfinal, int(tfinal/Ts)+1)

num = [0.0868*(1 - np.exp(-1.8*Ts)), 0.0868*(np.exp(-1.8*Ts) - np.exp(-3.6*Ts))]
den = [1, -np.exp(-3.6*Ts), 0]

G_motor = tf(num, den, Ts)

print(G_motor)

#
# rlocus(G_motor, plot=True, grid=True)
# plt.show()

Gint = tf(1, [1, 0])
Gtrap = c2d(Gint, Ts, method='forward_diff')


T_d = feedback((10+20*Gtrap)*G_motor, 1)

y, t = step(G_motor*6, tempo)
y2, t = step(T_d*0.5, tempo)


fig, axs = plt.subplots()
plt.step(t, y, where='post')
plt.step(t, y2, color=(1, 0, 0), where='post')
plt.show()


