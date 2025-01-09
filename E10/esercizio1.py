
import numpy as np
import scipy 
import matplotlib.pyplot as plt

import runw as rw
plt.subplots(figsize=(7,5))
xx5 = []
yy5 = []
step=1
n=1000
for i in range(5):
    x0,y0 =rw.randomwalk( n,step)
    xx5.append(x0)
    yy5.append(y0)
    plt.scatter(x0,y0, s=3)
plt.xlabel(r'$\Delta x$')
plt.ylabel(r'$\Delta y$')
plt.xlim(-200, 200)
plt.ylim(-200, 200)
plt.show()
xx100=[]
yy100=[]
for n0 in [10,100,1000]:
    for i in range(100):
        x0,y0 =rw.randomwalk( n0,step)
        xx100.append([x0,n0])
        yy100.append([y0,n0])
        plt.scatter(x0,y0, s=3)

plt.xlabel(r'$\Delta x$')
plt.ylabel(r'$\Delta y$')
plt.xlim(-200, 200)
plt.ylim(-200, 200)
plt.show()
fig, ax = plt.subplots(1,2, figsize=(7,5))
for i in range(5):
    ax[0].scatter(xx5[i],yy5[i], s=3)
    ax[1].plot(np.sqrt(xx5[i]**2+yy5[i]**2) )

ax[0].set_xlabel(r'$\Delta x$')
ax[0].set_ylabel(r'$\Delta y$')
ax[0].set_xlim(-200, 200)
ax[0].set_ylim(-200, 200)
ax[1].set_xlabel('step')
ax[1].set_ylabel(r'$d^2$')
ax[1].set_ylim(0, 250)
plt.show()
