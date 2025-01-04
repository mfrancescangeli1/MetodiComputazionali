import sys,os
import argparse
from  scipy import integrate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def pot(x):
    y=0.1*x**6
    return y
def periodo(x0):
    
    xx= np.arange(-5,5.05, 0.1)
    
    T=np.empty(len(xx))
    dx=0.1
    for i in range(1, len(xx) + 1):
        pot_diff = pot(x0) - pot(xx[:i]) 
    T1=np.sqrt(8)*integrate.simpson(1/(np.sqrt(pot_diff)),dx=dx)

    return T1
        

 
xx = np.arange(-5,5.05, 0.1)

'''
plt.plot(xx, 0.1*xx**6, color='slategray')

plt.axvline(color='k', linewidth=0.5)
plt.xlabel('x')
plt.ylabel(r'V(x)')
plt.plot(4.5, 0.1*4.5**6, 'o', markersize=12, color='tomato')
plt.show()
'''
plt.plot(xx, periodo(xx), color='slategray')

plt.axvline(color='k', linewidth=0.5)
plt.xlabel('x')
plt.ylabel(r'V(x)')
plt.show()
