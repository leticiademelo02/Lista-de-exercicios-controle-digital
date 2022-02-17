################################################################################################################
#
#               DIGITAL CONTROL - EE/UFSCAR
#
#   Author: André Carmona Hernandes
#   Version: 1
#   Last-Update: 07.03.2021
#
#   Info: Execute "Simpson" integration
#
#   These codes are used in DIGITAL CONTROL classes. You may use and study by them, however use with caution!
#
################################################################################################################

from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np


Ts = 0.1
time_final = 5
n_points = round(time_final / Ts) + 1

time = linspace(0, time_final, n_points)

y = 4 * time ** 3 + time
int_y = time ** 4 + 0.5 * time ** 2

print(int_y[-1])
#first attempt
gain = Ts/12
Integral = gain*(5*y[1]+8*y[0])
for k in range(2, n_points):
    aux = 5*y[k]+8*y[k-1] - y[k-2]
    Integral = Integral + gain*aux
print(Integral)

#second attempt
# Integral = gain*(14*y[1]-y[0])
# for k in range(2, n_points):
#     aux = 14*y[k] - y[k-1] - y[k-2]
#     Integral = Integral + gain*aux
# print(Integral)

#Simpson's rule
gain = Ts/3
Integral = gain*(y[1]+4*y[0])
for k in range(2, n_points, 2):
    aux = y[k] + 4 * y[k-1] + y[k-2]
    Integral = Integral + gain*aux
print(Integral)

g_c = tf([1, 1], [1, 3, 0])
g_simp = tf([1, 1], [1, 3])
print(g_c)
print(g_simp)
g_t = c2d(g_c, Ts, method='tustin')
print(g_t)
g_s = tf([6/(12+15*Ts), 7/(12+15*Ts), 1/(12+15*Ts), 0], [1, (9*Ts-24)/(12+15*Ts), (12-27*Ts)/(12+15*Ts), 3*Ts/(12+15*Ts)], Ts)
print(g_s)
simp_z = tf([12/Ts, -12/Ts, 0], [5, 8, -1], Ts)
g_simp_z = c2d(g_simp, Ts, method='tustin') / simp_z
print(g_simp_z)
y_cont, t = impulse(g_c, time, 0)
y_tust, t = impulse(g_t*(1/Ts), time, 0)
y_simp, t = impulse(g_simp_z*(1/Ts), time, 0)


fig, axs = plt.subplots()
axs.plot(time, y_cont, color=[0.5, 0.5, 0.5, 1], label="Continuo", linewidth=3.0)
axs.step(time, y_tust, color=(0, 1, 0, 0.5), label="Tustin", linewidth=3.0, where='post')
axs.step(time, y_simp, color=(1, 0, 0, 0.5), label="Simpson", linewidth=3.0, where='post')
legend = axs.legend(loc='best', shadow=True, fontsize='x-large')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.show()
