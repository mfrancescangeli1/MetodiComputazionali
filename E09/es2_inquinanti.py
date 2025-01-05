import numpy as np
import pandas as pd
from scipy import constants, fft
import matplotlib.pyplot as plt
data=pd.read_csv('copernicus_PG_selected.csv')

'''
tutti i graficini
'''
plt.plot(data['date']-data['date'][0],data['mean_co_ug/m3'], label='CO')
plt.plot(data['date']-data['date'][0],data['mean_nh3_ug/m3'], label='NH3')
plt.plot(data['date']-data['date'][0],data['mean_no2_ug/m3'], label='NO2')
plt.plot(data['date']-data['date'][0],data['mean_o3_ug/m3'], label='03')
plt.plot(data['date']-data['date'][0],data['mean_pm10_ug/m3'], label='pm10')
plt.plot(data['date']-data['date'][0],data['mean_pm2p5_ug/m3'], label='pm2p5')
plt.xlabel('Freq. [Hz]')
plt.ylabel('inquinanti')
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='lower left')
plt.show()
#analisi CO

c = fft.rfft(data['mean_co_ug/m3'].values)
freqs = fft.rfftfreq(len(data), d=1)
coam = np.argmax(np.absolute(c[1:len(c)//2]))+1
print('Massimo PS CO: {:f} - Freq {:f} - Periodo: {:d}'.format(np.absolute(c[coam])**2, freqs[coam], int(1/freqs[coam])) )
'''
frequenza e potenza
'''
plt.plot(freqs[:len(data)//2],np.absolute(c[:len(data)//2]**2))
plt.xlabel('Freq. [Hz]')
plt.ylabel('CO')
plt.xscale('log')
plt.yscale('log')
plt.show()
 #  le frequenze sono ordinate secondo l'ordine [0-->fmax, -fmax, 0[
            #  per produrre un grafico corretto si possono riordinare le frequenze con fft.fftshift
cofrshift = fft.fftshift(freqs)
copsshift = fft.fftshift(c)
plt.subplots(figsize=(10,7))
plt.title('CO')
plt.plot(cofrshift, copsshift)
#plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'f [$d^{-1}$]')
plt.ylabel(r'$|c_{FFT}|^2$')
plt.show()


