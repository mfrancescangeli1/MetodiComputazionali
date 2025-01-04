import numpy as np
import matplotlib.pyplot as plt
from  scipy import integrate
import math
import pandas as pd
dfvel=pd.read_csv('vel_vs_time.csv')
'''
plt.plot(dfvel['t'],dfvel['v'], alpha=0.3, color='gold', label='velocità')

plt.xlabel('tempo ',  fontsize=16)
plt.ylabel('velocità',  fontsize=16)
plt.legend(fontsize=14)
plt.show()
'''
dh=abs(dfvel['t'][1]-dfvel['t'][0])
dist=[]
for i in range(0,len(dfvel['t'])):
    s=integrate.simpson(dfvel['v'][0:i+1],dx=dh)
    dist.append(s)
dist=np.array(dist)
plt.plot(dfvel['t'],dist, alpha=0.3, color='gold', label='velocità')

plt.xlabel('tempo ',  fontsize=16)
plt.ylabel('velocità',  fontsize=16)
plt.legend(fontsize=14)
plt.show()
    
