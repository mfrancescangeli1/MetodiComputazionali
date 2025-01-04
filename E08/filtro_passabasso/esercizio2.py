
import numpy as np
import pandas as pd
from scipy import optimize
import matplotlib.pyplot as plt
from scipy import integrate
data=pd.read_csv('dati1.csv')



plt.plot(data['tempi'],data['V_out'])
plt.plot(data['tempi'],data['V_in'])
plt.xlabel('t')
plt.ylabel('Vout')

plt.ylim(-2,2)
plt.show()
