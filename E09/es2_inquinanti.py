import numpy as np
import pandas as pd
from scipy import constants, fft
import matplotlib.pyplot as plt
data=pd.read_csv('copernicus_PG_selected.csv')

'''
tutti i graficini
plt.plot(data['date'],data['mean_co_ug/m3'], label='CO')
plt.plot(data['date'],data['mean_nh3_ug/m3'], label='NH3')
plt.plot(data['date'],data['mean_no2_ug/m3'], label='NO2')
plt.plot(data['date'],data['mean_o3_ug/m3'], label='03')
plt.plot(data['date'],data['mean_pm10_ug/m3'], label='pm10')
plt.plot(data['date'],data['mean_pm2p5_ug/m3'], label='pm2p5')
plt.xlabel('Freq. [Hz]')
plt.ylabel('inquinanti')
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='lower left')
plt.show()
'''
c = fft.rfft(data['mean_co_ug/m3'].values)
freqs = fft.rfftfreq(len(data), d=1)
'''
frequenza e potenza
plt.plot(freqs[:len(data)//2],np.absolute(c[:len(data)//2]**2))
plt.xlabel('Freq. [Hz]')
plt.ylabel('CO')
plt.xscale('log')
plt.yscale('log')
'''
tempi=1/freqs
plt.plot(tempi[:len(data)//2],data['mean_co_ug/m3'][:len(data)//2], label='pm2p5')
plt.xlabel('Freq. [Hz]')
plt.ylabel('inquinanti')
plt.xscale('log')
plt.yscale('log')
plt.legend(loc='lower left')
plt.show()

plt.show()
