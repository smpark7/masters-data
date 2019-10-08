import math
import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import rcParams, cm
from pyne import serpent
from pyne import nucname

data = serpent.parse_det('msfr-full-core_det1b1.m')

r_pow = data['DETradialfissionR']
phi_pow = data['DETradialfissionPHI']
z_pow = data['DETradialfissionZ']
fissionr = data['DETradialfission']
n = len(r_pow) * len(phi_pow)
m = len(r_pow) * len(z_pow)
fissionr_den = np.reshape(fissionr.reshape((n,12))[:,10], \
                         (len(r_pow), len(phi_pow))) \
                         #/ max(fission.reshape((57600,12))[:,10])
#fissionz = data['DETfisxz']
#fissionz_den = np.reshape(fissionz.reshape((m,12))[:,10], \
#                         (len(z_pow), len(x_pow))) \
#
#
#fig, ax = plt.subplots(1,1,figsize=(12,10))
#c = ax.pcolor(fissionx_den,cmap=cm.viridis)
#fig.colorbar(c, ax=ax)
#plt.savefig("powerxy.png", dpi=600)
#
#fig, ax = plt.subplots(1,1,figsize=(12,10))
#c = ax.pcolor(fissionz_den,cmap=cm.viridis)
#fig.colorbar(c, ax=ax)
#plt.savefig("powerxz.png", dpi=600)

plt.figure(figsize=(12,10))
r = r_pow[:,2]
area = np.zeros(len(r_pow))
for i in range(len(r_pow)):
    area[i] = (r_pow[i,1] ** 2 - r_pow[i,0] ** 2) * np.pi
    fissionr_den[i] /= area[i]
plt.plot(r, fissionr_den)

data = serpent.parse_det('det-950k.m')

#x_pow = data