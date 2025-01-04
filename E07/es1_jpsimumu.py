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
def fg1(x,A,mu,sigma,p1,p0):
    '''
    fit gaussiana
    '''
    return A*np.exp(-0.5*(x-mu)**2/sigma**2)+p1*x+p0
def fg2(x,mu,A1,A2,sigma1,sigma2,p0,p1):
    '''
    fit doppia gaussiana
    '''
    return (A1*np.exp(-0.5*(x-mu)**2/sigma1**2)+
            A2*np.exp(-0.5*(x-mu)**2/sigma2**2))+p1*x+p0
#fit
pnames = None
params = None
params_covariance = None
y1fit  = None
y2fit = None
pnames = ['A', 'mu', 'sigma', 'p1', 'p0']
pstart = np.array([3, 100,  0.5, 10, -0.1])            
params,params_covariance=optimize.curve_fit(fg1,bincenter,n,sigma=np.sqrt(n),
                                            absolute_sigma=True,p0=[pstart])
scarti=(n-fg1(bincenter,params[0],params[1],params[2],params[3],params[4]))
scarti_norm=scarti/np.sqrt(n)
pnames2 = ['mu', 'A1', 'A2', 'sigma1', 'sigma2', 'p0', 'p1']
pstart2 = np.array([3, 200, 50, 0.5, 2,  10, -0.1])            
params2, params_covariance2 = optimize.curve_fit(fg2,bincenter,n, sigma=np.sqrt(n),
                                                 absolute_sigma=True,p0=[pstart2])
scarti2=(n-fg2(bincenter, params2[0], params2[1], params2[2],
               params2[3], params2[4], params2[5], params2[6]))
scarti2_norm=scarti2/np.sqrt(n)
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

fig, (axs1, axs2,axs3) = plt.subplots(3, 1,gridspec_kw={'height_ratios':[3,1,1]})
fig.suptitle('confronto dati doppia gaussiana')
n,bins, patches =axs1.hist(mass_inv, bins=200,range=[2.7,3.5])
axs1.set_xlabel('massa invariante (GeV)')
axs1.set_ylabel('n')
axs1.plot(bincenter,
         fg2(bincenter,params2[0],params2[1],params2[2],
             params2[3],params2[4],params2[5],params2[6]),
         color='red')
axs2.errorbar(bincenter, scarti2,fmt= '.',yerr=np.sqrt(n))
axs2.set_ylabel('scarti')
axs3.errorbar(bincenter, scarti2_norm,fmt= '.')
axs3.set_ylabel('scarti normalizzati')
plt.show()

