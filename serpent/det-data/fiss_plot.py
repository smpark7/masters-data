import math
import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import rcParams, cm
from pyne import serpent
from pyne import nucname

data = serpent.parse_det('msfr-full-core-det_det.m')

x_pow = data['DETfluxxyX']
y_pow = data['DETfluxxyY']
z_pow = data['DETfluxxyZ']
fissionx = data['DETfluxxy']
n = len(x_pow) * len(y_pow)
m = len(x_pow) * len(z_pow)
fissionx_den = np.reshape(fissionx.reshape((n,12))[:,10], \
                         (len(x_pow), len(y_pow))) \
                         #/ max(fission.reshape((57600,12))[:,10])
#fissionz = data['DETfisxz']
#fissionz_den = np.reshape(fissionz.reshape((m,12))[:,10], \
#                         (len(z_pow), len(x_pow))) \
#
#
fig1, ax1 = plt.subplots(1,1,figsize=(10,10))
c = ax1.pcolor(fissionx_den,cmap=cm.viridis)
fig1.colorbar(c, ax=ax)

fig2, ax2 = plt.subplots(1,1,figsize=(12,10))
d = ax2.plot(np.linspace(0,480,481), fissionx_den[240,:])

x_pow = data['DETfluxxzX']
y_pow = data['DETfluxxzY']
z_pow = data['DETfluxxzZ']
fissionz = data['DETfluxxz']
n = len(x_pow) * len(z_pow)
m = len(x_pow) * len(y_pow)
fissionz_den = np.reshape(fissionz.reshape((n,12))[:,10], \
                         (len(z_pow), len(x_pow))) \
                         #/ max(fission.reshape((57600,12))[:,10])
#fissionz = data['DETfisxz']
#fissionz_den = np.reshape(fissionz.reshape((m,12))[:,10], \
#                         (len(z_pow), len(x_pow))) \
#
#
fig1, ax1 = plt.subplots(1,1,figsize=(10,10))
c = ax1.pcolor(fissionz_den,cmap=cm.viridis)
fig1.colorbar(c, ax=ax)

fig2, ax2 = plt.subplots(1,1,figsize=(12,10))
d = ax2.plot(np.linspace(0,440,441), fissionz_den[:,240])

#plt.savefig("powerxy.png", dpi=600)
#
#fig, ax = plt.subplots(1,1,figsize=(12,10))
#c = ax.pcolor(fissionz_den,cmap=cm.viridis)
#fig.colorbar(c, ax=ax)
#plt.savefig("powerxz.png", dpi=600)

#plt.figure(figsize=(12,10))
#r = r_pow[:,2]
#area = np.zeros(len(r_pow))
#for i in range(len(r_pow)):
#    area[i] = (r_pow[i,1] ** 2 - r_pow[i,0] ** 2) * np.pi
#    fissionr_den[i] /= area[i]
#plt.plot(r, fissionr_den)
