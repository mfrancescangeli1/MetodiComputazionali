import numpy as np
import pandas as pd
from scipy import optimize
import matplotlib.pyplot as plt
data=pd.read_csv('Jpsimumu.csv')

mass_inv=np.sqrt((data['E1']+data['E2'])**2-(
                 (data['px1']+data['px2'])**2+
                 (data['py1']+data['py2'])**2+
                 (data['pz1']+data['pz2'])**2))


n,bins, patches =plt.hist(mass_inv, bins=200,range=[2.7,3.5])


bincenter=(bins[1:]+bins[:-1])/2
'''
plt.hist(mass_inv, bins=200, range=[2.75,3.50])
plt.title('distribuzione massa invariante')
plt.xlabel('massa invariante (GeV)')
plt.show()
'''
def fg1(x,A,mu,sigma,p1,p0):
    return A*np.power(np.e,-np.power(x-mu,2)/(2*np.power(sigma,2)))+p1*x+p0
params,params_covariance=optimize.curve_fit(fg1,bincenter,n,sigma=np.sqrt(n),
                                            absolute_sigma=True)
scarti=(n-fg1(bincenter,params[0],params[1],params[2],params[3],params[4]))
scarti_norm=scarti/np.sqrt(n)
print(params)
fig, (ax1, ax2,ax3) = plt.subplots(3, 1,gridspec_kw={'height_ratios':[3,1,1]})
fig.suptitle('confronto dati')
n,bins, patches =ax1.hist(mass_inv, bins=200,range=[2.7,3.5])

ax1.set_xlabel('massa invariante (GeV)')
ax1.set_ylabel('n')
ax1.plot(bincenter,
         fg1(bincenter,params[0],params[1],params[2],params[3],params[4]),
         color='red')


ax2.errorbar(bincenter, scarti,fmt= '.',yerr=np.sqrt(n))
ax2.set_ylabel('scarti')
ax3.errorbar(bincenter, scarti_norm,fmt= '.')
ax3.set_ylabel('scarti normalizzati')
plt.show()
expect1=fg1(bincenter,params[0],params[1],params[2],params[3],params[4])
chi2=np.sum(np.power(scarti,2)/expect1)
print(chi2)
