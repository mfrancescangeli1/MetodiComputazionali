import numpy as np
import pandas as pd

from scipy import constants, fft
import scipy
import matplotlib.pyplot as plt
data1=pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/data_sample1.csv')
data2=pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/data_sample2.csv')
data3=pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/data_sample3.csv')
fig, ax = plt.subplots()
'''
ax.plot(data1['time'], data1['meas'], label='data 1')
ax.plot(data2['time'], data2['meas'],label='data2')
ax.plot(data3['time'], data3['meas'],label='data3')
ax.set_xlabel('Time (s)')
ax.set_ylabel('meas')

'''
def rumore(freq,k,beta):
    return k/(freq**beta)
#analisi di Fourier
c1  = fft.fft(data1['meas'].values)
freqs1 = fft.fftfreq(len(data1), d=1)
c2  = fft.rfft(data2['meas'].values)
freqs2 = fft.rfftfreq(len(data2), d=1)
c3  = fft.rfft(data3['meas'].values)
freqs3 = fft.rfftfreq(len(data3), d=1)
pnames=['k','beta']
#fit dei dati
params1, params_covariance1=scipy.optimize.curve_fit(
    rumore,freqs1[3:len(data1)//2],c1[3:len(data1)//2],p0=[1, 1])

print(params1,params_covariance1.diagonal())
plt.plot(freqs1[3:len(data1['meas'])//2],
         np.absolute(c1[3:len(data1)//2])**2, label='data1')
plt.plot(freqs1[3:len(data1['meas'])//2],
         rumore(freqs1[3:len(data2)//2],params1[0],params1[1]), label='fit')
'''
plt.plot(freqs2[:len(data2['meas'])//2],
         np.absolute(c2[:len(data1)//2])**2, label='data2')
plt.plot(freqs3[:len(data3['meas'])//2],
         np.absolute(c3[:len(data1)//2])**2, label='data3')
'''
plt.xlabel('Freq. [Hz]')
plt.ylabel(r'$\left| c_k \right|^2$')
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='lower left')
plt.show()
