import numpy as np
import pandas as pd
from scipy import optimize
import matplotlib.pyplot as plt
from scipy import integrate

def dvout(Vout, t,RC,vin):
    return (1/RC)*(vin(t)-Vout)
def vin_square(t):
    if np.isscalar(t):
        if int(t)%2==0:
            return 1
        else:
            return -1
    else:
        vin = np.ones(len(t))
        odd_mask = tt.astype(int) %2 != 0
        vin[odd_mask] = -1
        return vin
    #intervallo [a,b]. x di partenza = 0.

tt = np.linspace(0,10,1000)
x0 =  0.
RC=[0.25,1,4]
# Dizionari per soluzioni
xsolsp = {}


# Ciclo diversi valori di N
for rc in RC: 

    # Calcolo solzuine tramite scipy.integrate.odeint
    xx = integrate.odeint(dvout, y0=x0, t=tt,args=(rc,vin_square))
    # Aggiunta delle soluzioni al dizionario
    xsolsp.update({rc : xx})
data=pd.DataFrame(columns=['tempi', 'V_in', 'V_out'])
data['tempi']=tt
data['V_in']=vin_square(tt)
data['V_out']=xx
pd.DataFrame.to_csv(data,'dati1.csv')
for rc in RC:
    plt.plot(tt,xsolsp[rc],label=' RC= {:}'.format(rc))
plt.plot(tt,vin_square(tt),label='$V_{in}$')
plt.xlabel('t')
plt.ylabel('Vout')
plt.legend(fontsize=10)
plt.ylim(-2,2)
plt.show()
