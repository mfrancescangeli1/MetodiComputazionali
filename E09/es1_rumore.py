import numpy as np
import pandas as pd
from scipy import constants, fft
import scipy
import matplotlib.pyplot as plt
data1=pd.read_csv('data_sample1.csv')
data2=pd.read_csv('data_sample2.csv')
data3=pd.read_csv('data_sample3.csv')
'''
grafico segnali
'''
fig,ax = plt.subplots(figsize=(9,6))

plt.plot(data1['time'], data1['meas'], color='cyan',      label='Sample 1')
plt.plot(data2['time'], data2['meas'], color='limegreen', label='Sample 2')
plt.plot(data3['time'], data3['meas'], color='orange',    label='Sample 3')
plt.legend()
plt.xlabel('time [s]')
plt.xlabel('Signal')
plt.show()
def rumore(freq,k,beta):
    return k/(freq**beta)
#analisi di Fourier
dt1=data1['time'][1]-data1['time'][0]
c1  = fft.fft(data1['meas'].values)
freqs1 = fft.fftfreq(len(data1), d=dt1)
dt2=data2['time'][1]-data2['time'][0]
c2  = fft.fft(data2['meas'].values)
freqs2 = fft.fftfreq(len(data2), d=dt2)
dt3=data3['time'][1]-data3['time'][0]
c3  = fft.fft(data3['meas'].values)
freqs3 = fft.fftfreq(len(data3), d=dt3)
#grafico spettro di potenza
fig,ax = plt.subplots(figsize=(9,6))
plt.plot( freqs1[:len(c1)//2], np.absolute(c1[:len(c1)//2])**2,
          color='cyan',label='Sample 1')
plt.plot( freqs2[:len(c2)//2], np.absolute(c2[:len(c2)//2])**2,
          color='limegreen', label='Sample 2')
plt.plot( freqs3[:len(c3)//2], np.absolute(c3[:len(c3)//2])**2,
          color='orange', label='Sample 3')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('f [Hz]')
plt.ylabel(r'$\left| c_k\right|^2$')
plt.legend()
plt.show()

#fit dei dati
params1, params_covariance1=scipy.optimize.curve_fit(
    rumore,freqs1[2:len(c1)//2],np.absolute(c1[2:len(c1)//2])**2, p0=[1, 1])
print(params1,params_covariance1.diagonal())
fig,ax = plt.subplots(figsize=(9,6))
plt.plot(freqs1[:len(c1)//2],
         np.absolute(c1[:len(c1)//2])**2,color='orange', label='data1')
plt.plot(freqs1[1:len(c1)//2],
         rumore(freqs1[1:len(c1)//2],params1[0],params1[1]),
         color='darkred', label='fit')
plt.xlabel('Freq. [Hz]')
plt.ylabel(r'$\left| c_k \right|^2$')
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='lower left')
plt.show()
params2, params_covariance2=scipy.optimize.curve_fit(
    rumore,freqs2[5:len(c2)//2],np.absolute(c2[5:len(c2)//2])**2, p0=[1, 1])
plt.plot(freqs2[:len(c2)//2],
         np.absolute(c2[:len(c2)//2])**2,color='cyan', label='data2')
plt.plot(freqs2[1:len(c2)//2],
         rumore(freqs2[1:len(c2)//2],params2[0],params2[1]),
         color='darkblue', label='fit')
plt.xlabel('Freq. [Hz]')
plt.ylabel(r'$\left| c_k \right|^2$')
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='lower left')
plt.show()
params3, params_covariance3=scipy.optimize.curve_fit(
    rumore,freqs3[5:len(c3)//2],np.absolute(c3[5:len(c3)//2])**2, p0=[1, 1])
plt.plot(freqs3[:len(c3)//2],
         np.absolute(c3[:len(c3)//2])**2,color='yellow', label='data3')
plt.plot(freqs3[1:len(c3)//2],
         rumore(freqs3[1:len(c3)//2],params3[0],params3[1]),
         color='gold', label='fit')
plt.xlabel('Freq. [Hz]')
plt.ylabel(r'$\left| c_k \right|^2$')
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='lower left')
plt.show()
