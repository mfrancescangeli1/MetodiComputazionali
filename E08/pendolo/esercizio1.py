
import numpy as np
import pandas as pd
from scipy import optimize
import matplotlib.pyplot as plt
from scipy import integrate
def drdt_pendolo(r, t, l,g):
    dthdt=r[1]
    dwdt=(-g/l)*np.sin(r[0])
    return (dthdt,dwdt)
time_vec = np.linspace(0, 10, 100)
l=0.5
g=9.81
th0=3.14/4
yinit = ( th0,0)
yarr  = integrate.odeint(drdt_pendolo, yinit, time_vec, args=(l,g))
fig,ax = plt.subplots(figsize=(9,6))
plt.plot(time_vec,  yarr, label=('x', 'v'))
plt.legend(fontsize=14)
plt.show()
