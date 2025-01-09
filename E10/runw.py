import numpy as np
import scipy 
import matplotlib.pyplot as plt
def randomwalk(N, s):
    phi= np.random.uniform(low=0, high=2*np.pi, size=N)
    dx = np.array([0])
    dy = np.array([0])
    for i in phi:
        tx = dx[-1] + s*np.cos(i)
        ty = dy[-1] + s*np.sin(i)
        dx = np.append(dx, tx)
        dy = np.append(dy, ty) 
    return dx, dy
def phi(N):
    # valore random per cumulativa 
    cum = np.random.random(N)
    # phi da inversa cumulativa
    phi = 2*np.arccos(1-2*cum)
    return phi
def pphi(phi):
    return np.sin(phi/2)/4
def randomasimm(s,sf):
    dx = np.array([0])
    dy = np.array([0])
    while dx[-1]<s*100:
        phi= np.random.uniform(low=0, high=2*np.pi)
        tx = dx[-1] + s*np.cos(phi)+sf
        ty = dy[-1] + s*np.sin(phi)
        dx = np.append(dx, tx)
        dy = np.append(dy, ty)
    return dx, dy
    
'''
def phi_distribution():

    
    # array con valori di phi per grafico p(phi)
    xphi = np.arange(0, 2*np.pi, 0.1)

    # Grafico p(phi)
    plt.plot(xphi, pphi(xphi) )
    plt.xlabel(r'$\varphi$ [rad]')
    plt.ylabel(r'p($\varphi$)')
    plt.show()
    
    
    #----------------------------------------------------------#
    # Genrazione distribuzione secondo p(phi)
    #----------------------------------------------------------#
    
    N = 100000    # eventi generati
    
    phibins = 99  # numero bin per histogramma phi
    binw = (2*np.pi/phibins)  #largezza bin
    
    # Fattori di conversione fra altezza bin e probabilità 
    p2n = N*binw  # fattore di conversione da probabilità ad altezza bin
    n2p = 1/p2n   # fattore di conversione da altezza bin a probabilità 

    # Genero N valori di phi secondo la distrbuzione di probabilità p(phi)
    myphi = phi(N)


    
    # Istogramma valori di phi generati  con sovrapposta la curva di valori attesi da p2n*pphi(phi)
    nb,xbins,_ = plt.hist(myphi, bins=phibins, label='MC' )
    plt.plot(xphi, p2n*pphi(xphi),  label=r'$N \cdot p(\varphi) d\varphi$')
    plt.xlabel(r'$\varphi$ [rad]')
    plt.ylabel(r'Eventi')
    plt.legend(fontsize=14)
    plt.show()

    #print(nb)
    #print(xbins)



    # Istogramma valori di phi generati riscalati per rappresentare la probabilità 
    xc = (xbins[:-1]+xbins[1:])/2
    plt.plot(xc, nb*n2p,       label=r'$nb /(N \cdot d\varphi$)')
    plt.plot(xphi, pphi(xphi), label=r'$p(\varphi)$')
    plt.xlabel(r'$\varphi$ [rad]')
    plt.ylabel(r'$p(\varphi)$')
    plt.legend(fontsize=14)
    plt.show()

    

    # Istogramma valori di phi generati espressi in gradi
    plt.hist(np.rad2deg(myphi), bins=90)
    plt.xlabel(r'$\varphi$ [deg]')
    plt.ylabel(r'')
    plt.show()
phi_distribution()    
'''
