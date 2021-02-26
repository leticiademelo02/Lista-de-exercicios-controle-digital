################################################################################################################
#
#               DIGITAL CONTROL - EE/UFSCAR
#
#   Author: André Carmona Hernandes
#   Version: 1
#   Last-Update: 24.02.2021
#
#   Info: Function to show comparison between Forward s approximations
#
#   These codes are used in DIGITAL CONTROL classes. You may use and study by them, however use with caution!
#
################################################################################################################

from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np

# Compensador D(s) = Y/U, s-1/s^2+3s+2
Ts = 0.1
time_final = 5
Npoints = round(time_final / Ts) + 1
sys = tf([1, -1], [1, 3, 2])

time = np.linspace(0, time_final, Npoints)
y_cont, time = step(sys, time, 0)

control_action = np.ones(Npoints)
y_forward = np.zeros(Npoints)
y_backward = np.zeros(Npoints)
# y_centered = np.zeros(Npoints)
counter = 0
for t in time:
    if counter == 0:
        y_forward[counter] = (1 / (1 + 2 * Ts)) * (Ts * control_action[counter])
        y_backward[counter] = (1 / (1 + 3 * Ts + 2 * Ts ** 2)) * ((Ts - Ts ** 2) * control_action[counter])
    elif counter == 1:
        y_forward[counter] = (1 / (1 + 2 * Ts)) * (
                Ts * control_action[counter] - (Ts + Ts ** 2) * control_action[counter - 1]
                - (3 * Ts ** 2 - 2 * Ts - 2) * y_forward[counter - 1])
        y_backward[counter] = (1 / (1 + 3 * Ts + 2 * Ts ** 2)) * (
                (Ts - Ts ** 2) * control_action[counter] - Ts * control_action[counter - 1]
                + (2 + 3 * Ts) * y_backward[counter - 1])
        # y_centered[counter] = 2 * Ts * control_action[counter - 1] - 4 * Ts * y_centered[counter - 1]
    elif counter == 2:
        y_forward[counter] = (1 / (1 + 2 * Ts)) * (
                Ts * control_action[counter] - (Ts + Ts ** 2) * control_action[counter - 1]
                - (3 * Ts ** 2 - 2 * Ts - 2) * y_forward[counter - 1] - y_forward[counter - 2])
        y_backward[counter] = (1 / (1 + 3 * Ts + 2 * Ts ** 2)) * (
                (Ts - Ts ** 2) * control_action[counter] - Ts * control_action[counter - 1]
                + (2 + 3 * Ts) * y_backward[counter - 1] - y_backward[counter - 2])
        # y_centered[counter] = 2 * Ts * control_action[counter - 1] - 4 * Ts ** 2 * control_action[counter - 2] \
        #                       - 4 * Ts * y_centered[counter - 1] - (12 * Ts ** 2 - 2) * y_centered[counter - 2]
    elif counter == 3:
        y_forward[counter] = (1 / (1 + 2 * Ts)) * (
                Ts * control_action[counter] - (Ts + Ts ** 2) * control_action[counter - 1]
                - (3 * Ts ** 2 - 2 * Ts - 2) * y_forward[counter - 1] - y_forward[counter - 2])
        y_backward[counter] = (1 / (1 + 3 * Ts + 2 * Ts ** 2)) * (
                (Ts - Ts ** 2) * control_action[counter] - Ts * control_action[counter - 1]
                + (2 + 3 * Ts) * y_backward[counter - 1] - y_backward[counter - 2])
        # y_centered[counter] = 2 * Ts * control_action[counter - 1] - 4 * Ts ** 2 * control_action[counter - 2]
        # - 2 * Ts * control_action[counter - 3] - 4 * Ts * y_centered[counter - 1] - (12 * Ts ** 2 - 2) * y_centered[
        #     counter - 2] + 4*Ts*y_centered[counter-3]
    elif counter == 4:
        y_forward[counter] = (1 / (1 + 2 * Ts)) * (
                Ts * control_action[counter] - (Ts + Ts ** 2) * control_action[counter - 1]
                - (3 * Ts ** 2 - 2 * Ts - 2) * y_forward[counter - 1] - y_forward[counter - 2])
        y_backward[counter] = (1 / (1 + 3 * Ts + 2 * Ts ** 2)) * (
                (Ts - Ts ** 2) * control_action[counter] - Ts * control_action[counter - 1]
                + (2 + 3 * Ts) * y_backward[counter - 1] - y_backward[counter - 2])
        # y_centered[counter] = 2 * Ts * control_action[counter - 1] - 4 * Ts ** 2 * control_action[counter - 2]
        # - 2 * Ts * control_action[counter - 3] - 4 * Ts * y_centered[counter - 1] - (12 * Ts ** 2 - 2) * y_centered[
        #     counter - 2] + 4*Ts*y_centered[counter-3] - y_centered[counter-4]
    else:
        y_forward[counter] = (1 / (1 + 2 * Ts)) * (
                Ts * control_action[counter] - (Ts + Ts ** 2) * control_action[counter - 1]
                - (3 * Ts ** 2 - 2 * Ts - 2) * y_forward[counter - 1] - y_forward[counter - 2])
        y_backward[counter] = (1 / (1 + 3 * Ts + 2 * Ts ** 2)) * (
                (Ts - Ts ** 2) * control_action[counter] - Ts * control_action[counter - 1]
                + (2 + 3 * Ts) * y_backward[counter - 1] - y_backward[counter - 2])
        # y_centered[counter] = 2 * Ts * control_action[counter - 1] - 4 * Ts ** 2 * control_action[counter - 2]
        # - 2 * Ts * control_action[counter - 3] - 4 * Ts * y_centered[counter - 1] - (12 * Ts ** 2 - 2) * y_centered[
        #     counter - 2] + 4*Ts*y_centered[counter-3] - y_centered[counter-4]

    counter = counter + 1

fig, ax = plt.subplots()
plt.plot(time, y_cont, color=[0.5, 0.5, 0.5, 1], label="Contínuo", linewidth=3.0)
plt.step(time, y_forward, 'r', label="Para Frente", linewidth=3.0, where='post')
plt.step(time, y_backward, 'g', label="Para Trás", linewidth=3.0, where='post')
# plt.plot(time, y_centered, 'b', label="Centrado", linewidth=3.0)
legend = ax.legend(loc='best', shadow=True, fontsize='x-large')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.show(block=True)
