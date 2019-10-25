import math
import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import rcParams, cm
from pyne import serpent
from pyne import nucname

#data = serpent.parse_det('msfr-full-core-flux_det0.m')

x_pow = data['DETfluxxyX']
y_pow = data['DETfluxxyY']
z_pow = data['DETfluxxyZ']
fluxxy = data['DETfluxxy']
fluxxy_den = {}
n = len(x_pow) * len(y_pow)
m = len(x_pow) * len(z_pow)
fluxxy_tot = np.zeros((len(x_pow), len(y_pow)))
for i in range(6):
    fluxxy_den[i] = np.reshape(fluxxy[i*n:(i+1)*n,:].reshape((n,12))[:,10], \
                              (len(x_pow), len(y_pow)))
    fluxxy_tot = fluxxy_tot + fluxxy_den[i]
#fissionz = data['DETfisxz']
#fissionz_den = np.reshape(fissionz.reshape((m,12))[:,10], \
#                         (len(z_pow), len(x_pow))) \
#
#
fig1, ax1 = plt.subplots(1,1,figsize=(6,5))
c = ax1.pcolor(fluxxy_den[0],cmap=cm.viridis)
ax1.set_title('Group 6 flux')
ax1.set_xlabel('x [cm]')
ax1.set_ylabel('y [cm]')
fig1.colorbar(c, ax=ax1)

fig2, ax2 = plt.subplots(1,1,figsize=(6,5))
c = ax2.pcolor(fluxxy_tot,cmap=cm.viridis)
ax2.set_title('Total flux')
ax2.set_xlabel('x [cm]')
ax2.set_ylabel('y [cm]')
fig2.colorbar(c, ax=ax2)

fig3, ax3 = plt.subplots(1,1,figsize=(7,5))
c = ax3.plot(x_pow[:,0],fluxxy_tot[:,0])
ax3.set_title('Total radial flux')
ax3.set_xlabel('r [cm]')
ax3.set_ylabel('Flux [# s-1]')
        
fig4, ax4 = plt.subplots(1,1,figsize=(7,5))
for i in range(6):
    c = ax4.plot(x_pow[:,0],fluxxy_den[i][:,0],label='Group '+str(i+1))
#    c = ax4.plot(x_pow[:,0],fluxxy_tot[:,0])
ax4.set_title('Radial flux')
ax4.set_xlabel('r [cm]')
ax4.set_ylabel('Flux [# s-1]')
ax4.legend()

#fig1.colorbar(c, ax=ax1)

#fig2, ax2 = plt.subplots(1,1,figsize=(12,10))
#d = ax2.plot(np.linspace(0,480,481), fissionx_den[240,:])

r_pow = data['DETfluxrzR']
phi_pow = data['DETfluxrzPHI']
z_pow = data['DETfluxrzZ']
fluxrz = data['DETfluxrz']
fluxrz_den = {}
n = len(r_pow) * len(z_pow)
m = len(r_pow) * len(phi_pow)
fluxrz_tot = np.zeros((len(r_pow),len(z_pow)))
for i in range(6):
    fluxrz_den[i] = np.reshape(fluxrz[i*n:(i+1)*n,:].reshape((n,12))[:,10], \
                         (len(z_pow), len(r_pow)))
    fluxrz_tot = fluxrz_tot + fluxrz_den[i]
                         #/ max(fission.reshape((57600,12))[:,10])
#fissionz = data['DETfisxz']
#fissionz_den = np.reshape(fissionz.reshape((m,12))[:,10], \
#                         (len(z_pow), len(x_pow))) \
#
#
fig1, ax1 = plt.subplots(1,1,figsize=(7,5))
#c = ax1.pcolor(fissionz_den,cmap=cm.viridis)
for i in range(6):
#    c = ax1.plot(z_pow[:,0],fluxrz_tot)
    c = ax1.plot(z_pow[:,0],fluxrz_den[i],label='Group '+str(i+1))
ax1.legend()
ax1.set_title('Axial flux')
ax1.set_xlabel('z [cm]')
ax1.set_ylabel('Flux [# s-1]')
#fig1.colorbar(c, ax=ax)

#fig2, ax2 = plt.subplots(1,1,figsize=(12,10))
#d = ax2.plot(np.linspace(0,440,441), fissionz_den[:,240])

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
