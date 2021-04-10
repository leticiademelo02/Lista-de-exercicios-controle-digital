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

t_cont = 0.00001
Ts = 0.01
tfinal = 0.5
tempo = linspace(0, tfinal, int(tfinal/t_cont)+1)

G_motor = tf([12149], [1, 21])
print(G_motor)
y, t = step(G_motor*6, tempo)

tau_idx = np.where(np.abs(t-1/21) < 0.000005)
#
# fig, axs = plt.subplots()
# plt.plot(t, y, linewidth=5)
#
# xdata = [tempo[tau_idx], tempo[-1]]
# ydata = [y[tau_idx], y[-1]]
#
# bbox = dict(boxstyle="round", fc="0.8")
# arrowprops = dict(
#     arrowstyle="->",
#     connectionstyle="angle,angleA=0,angleB=-90,rad=10")
#
# offset = 10
# axs.annotate(
#     f'(t, w) = ({xdata[1]:1.2f}, {ydata[1]:1.2f})',
#     (xdata[1], ydata[1]),
#     xytext=(-15*offset, -4*offset), textcoords='offset points',
#     bbox=bbox, arrowprops=arrowprops)
# axs.annotate(
#     f'(t, w) = ({xdata[0]}, {ydata[0]})',
#     (xdata[0], ydata[0]),
#     xytext=(3*offset, -2*offset), textcoords='offset points',
#     bbox=bbox, arrowprops=arrowprops)

# plt.show()
#
# Ts_camera = 0.03
# MA_camera = c2d(G_motor, Ts_camera, method='zoh')
# print(MA_camera)
# t_camera = linspace(0, tfinal, int(tfinal/Ts_camera)+1)
# yc, tc = step(MA_camera*6, t_camera)
# y2, tc = step(MA_camera*4, t_camera)
# fig2, axs2 = plt.subplots()
# plt.step(tc, yc, where='post', linewidth=3)
# plt.step(tc, y2, color='r', where='post', linewidth=3)
# # plt.show()
#
# G_x_reta = G_motor*tf([0.035/100], [1, 0])
# y, t = step(G_x_reta*6, tempo)
# fig3, axs3 = plt.subplots()
# plt.plot(t, y, linewidth=5)
# plt.show()
###
#
t_ctr = linspace(0, tfinal, int(tfinal/Ts)+1)
Ga = tf([0.1*578.52, 0.09*578.52], [1, -0.81058, 0], Ts)
# G_ct = c2d(G_motor, Ts, method='zoh')
# y_4, t = step(G_motor*4, tempo)
# yctr, tc = step(G_ct*4, t_ctr)
ya, ta = step(Ga*4, t_ctr)
# fig4, axs4 = plt.subplots()
# plt.plot(t, y_4, color=(0.5, 0.5, 0.5, 0.8), linewidth=2, label='cont')
# plt.step(tc, yctr, color=(1, 0, 0, 0.8), where='post', linewidth=3, label='sem atraso')
# plt.step(ta, ya, color=(0, 0, 1, 0.8), where='post', linewidth=3, label='com atraso')
# plt.legend()
# plt.show()

#
K_norm = 1/578.52

# se descconsiderar a tensão de entrada, esse tá ok
# P = K_norm*2.88
# Ki = P/0.048
# Kd = P*0.005
#

P = K_norm*1.2
Ki = P/0.04
Kd = P*0.0008

Ac = (2*Ts*P+Ki*Ts**2+2*Kd)/(2*Ts)
Bc = (Ki*Ts**2-2*Ts*P-4*Kd)/(2*Ts)
Cc = Kd/Ts

C = tf([Ac, Bc, Cc], [1, -1, 0], Ts)
# C_int = tf(1, [1, 0])
# C_dev = tf([1/Ts, -1/Ts], [1, 0], Ts)
# C_pi = parallel(tf([Kp], [1], Ts), c2d(C_int*Kp/ti, Ts, method='tustin'))
MF_cont = feedback(Ga*C, 1)
C_MF = C/(1+Ga*C)
print(MF_cont, C_MF)
y_mf, tmf = step(MF_cont*2340, t_ctr)
u_c, tu = step(C_MF*2340, t_ctr)
fig5, axs5 = plt.subplots(1, 2)
axs5[0].step(ta, ya, color=(0, 0, 1, 0.8), where='post', linewidth=3, label='com atraso')
axs5[0].step(tmf, y_mf, color=(0, 1, 0, 0.8), where='post', linewidth=3, label='malha fechada')
axs5[0].plot([0.066, 0.066], [0, 3000], color=(0.6, 0.6, 0.6, 0.5))
axs5[0].plot([0, tfinal], [2200, 2200], color=(0.6, 0.6, 0.6, 0.5))
axs5[0].legend()
axs5[1].step(tmf, u_c, color=(0, 1, 0, 0.8), where='post', linewidth=3, label='Tensão')
axs5[1].legend()
plt.show()


