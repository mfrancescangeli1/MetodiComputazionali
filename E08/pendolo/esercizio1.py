
import numpy as np
import pandas as pd
from scipy import optimize
import matplotlib.pyplot as plt
from scipy import integrate
def drdt_pendolo(r, t, l):
    dthdt=r[1]
    dwdt=(-9.81/l)*np.sin(r[0])
    return (dthdt,dwdt)

l1=0.5 
l2=1.0
theta0 = np.radians(45)
omega0 = 0
yinit = (theta0, omega0)
yinit1 = (theta0*2/3, omega0)
dt = 0.01
ptimes = np.arange(0, 5, dt)

yarr1  = integrate.odeint(drdt_pendolo, yinit,ptimes, args=(l1,))
yarr2  = integrate.odeint(drdt_pendolo, yinit1,ptimes, args=(l1,))
yarr3  = integrate.odeint(drdt_pendolo, yinit,ptimes, args=(l2,))

fig,ax = plt.subplots(figsize=(9,6))
plt.plot(ptimes,  np.degrees(yarr1[:,0]), label='l1,th0')
plt.plot(ptimes, np.degrees(yarr2[:,0]), label='l1,th1')
plt.plot(ptimes,  np.degrees(yarr3[:,0]), label='l2,th0')
plt.xlabel('t')
plt.ylabel(r'$\theta$  [deg]')
plt.legend()
plt.show()
