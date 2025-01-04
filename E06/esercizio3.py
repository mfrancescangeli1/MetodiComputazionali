import sys,os
import argparse
from  scipy import integrate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def differenza_centrale(x, y, nh):
    d = y[nh:] - y[:-nh]
    h = x[nh:] - x[:-nh]
    
    for i in range(int(nh/2)):
        d = np.append(y[nh-i-1]-y[0], d)
        d = np.append(d, y[-1]-y[-(nh-i)])
    
        h = np.append(x[nh-i-1]-x[0], h)
        h = np.append(h, x[-1]-x[-(nh-i)])
    
    print('d=', d)
    print('h=', h)
    return d/h
def main():
     df = pd.read_csv('oscilloscope.csv')
     print( df.columns)
     plt.plot(df['time'], df['signal1'], color='maroon',   label='Canale 1')
     plt.plot(df['time'], df['signal2'], color='blueviolet',  label='Canale 2')
     plt.legend(fontsize=14)
     plt.xlabel('t [ns]')
     plt.ylabel('V [mV]')
     plt.show()
     dc100_ch1 = differenza_centrale(df['time'].to_numpy(),
                                   df['signal1'].to_numpy(), 2)  
     dc100_ch2 = differenza_centrale(df['time'].to_numpy(),
                                   df['signal2'].to_numpy(), 2)
     
     plt.plot(df['time'], dc100_ch1, color='maroon',   label='Canale 1')
     plt.plot(df['time'], dc100_ch2, color='blueviolet',  label='Canale 2')   
     plt.legend(fontsize=14)
     plt.xlabel('t [ns]')
     plt.ylabel('V/s [mV/ns]')
     plt.show()
if __name__ == "__main__":

    main()
