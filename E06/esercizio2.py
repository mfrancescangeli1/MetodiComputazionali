import sys,os
import argparse
from  scipy import integrate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def pot6(x,c):
    '''
    energia potenziale V=x^6
    '''
    return c*x**6
def pot4(x,c):
    '''
    energia potenziale V=x^4
    '''
    return c*x**4
def pot2(x,c):
    '''
    energia potenziale V=x^2
    '''
    return c*x**2
def pot(x,c):
    '''
    energia potenziale V=|x|^2/2
    '''
    return c*np.power(np.abs(x), 1.5)
def parse_arguments():
    parser = argparse.ArgumentParser(description='periodo oscillatori anarmonici.')
    parser.add_argument('--v6',    action='store_true', help='V = c*x^6')
    parser.add_argument('--v4',    action='store_true', help='V = c*x^4')
    parser.add_argument('--v2',    action='store_true', help='V = c*x^2')
    parser.add_argument('--v15',   action='store_true', help='V = c*|x|^3/2')
    parser.add_argument('--vall',  action='store_true', help='Confronto diversi potenziali')
    return  parser.parse_args()

        
def oscillatore():
    args = parse_arguments()
    vc=1
    m=1
    a=np.empty(0)
    T15 = np.empty(0)
    T2  = np.empty(0)
    T4  = np.empty(0)
    T6  = np.empty(0)
    dx=0.001
    for x0 in np.arange(0.5,6, 0.1):
        a  = np.append(a, x0)
        xx = np.arange(0, x0, dx)

        # 1/sqrt(V(x0) - V(x))
        integrand6  = 1./np.sqrt(pot6(x0, vc)  - pot6(xx, vc))
        integrand4  = 1./np.sqrt(pot4(x0, vc)  - pot4(xx, vc))
        integrand2  = 1./np.sqrt(pot2(x0, vc)  - pot2(xx, vc))
        integrand15 = 1./np.sqrt(pot(x0, vc) - pot(xx, vc))
        # Integrali 
        integral6  = integrate.simpson(integrand6,  dx=dx)
        integral4  = integrate.simpson(integrand4,  dx=dx)
        integral2  = integrate.simpson(integrand2,  dx=dx)
        integral15 = integrate.simpson(integrand15, dx=dx)
        #periodi
        T6  = np.append( T6,  np.sqrt(8*m) * integral6 )
        T4  = np.append( T4,  np.sqrt(8*m) * integral4 )
        T2  = np.append( T2,  np.sqrt(8*m) * integral2 )
        T15 = np.append( T15, np.sqrt(8*m) * integral15)
    Tarm = 2*np.pi *np.sqrt(m/(2*vc))
    #grafici
    if args.v6 == True:
        fig,ax = plt.subplots(2,1, figsize=(10, 10) )
        ax[0].plot(a, T6,   color='maroon',   label='V(x)=c$x^6$')
        ax[0].axhline(Tarm, color='royalblue',    label='$2 \pi \sqrt{2c/m}$')

        ax[0].legend(loc='upper center')
        ax[0].set_xlabel(r'$x_0$ [m]')
        ax[0].set_ylabel(r'T [s]')
        ax[0].set_ylim(0, 15)

        xa = np.linspace(-1.15, 1.15, 100)
        ax[1].plot(xa, pot6(xa, vc),   color='maroon',   label='V(x)=c$x^6$')
        ax[1].legend()
        ax[1].set_xlabel(r'$x$ [m]')
        ax[1].set_ylabel('V [J]')
        plt.show()
    if args.v4 == True:
        fig,ax = plt.subplots(2,1, figsize=(10, 10) )
        ax[0].plot(a, T4,   color='maroon',   label='V(x)=c$x^4$')
        ax[0].axhline(Tarm, color='royalblue',    label='$2 \pi \sqrt{2c/m}$')
        ax[0].legend(loc='upper center')
        ax[0].set_xlabel(r'$x_0$ [m]')
        ax[0].set_ylabel(r'T [s]')
        ax[0].set_ylim(0, 15)
  
        xa = np.linspace(-1.15, 1.15, 100)
        ax[1].plot(xa, pot4(xa, vc),   color='maroon',   label='V(x)=c$x^4$')
        ax[1].legend()
        ax[1].set_xlabel(r'$x$ [m]')
        ax[1].set_ylabel('V [J]')
        plt.show()
    if args.v2 == True:
        fig,ax = plt.subplots(2,1, figsize=(10, 10) )
        ax[0].plot(a, T2,   color='maroon',   label='V(x)=c$x^6$')
        ax[0].axhline(Tarm, color='royalblue',   label='$2 \pi \sqrt{2c/m}$')
        ax[0].legend(loc='upper center')
        ax[0].set_xlabel(r'$x_0$ [m]')
        ax[0].set_ylabel(r'T [s]')
        ax[0].set_ylim(0, 15)
        xa = np.linspace(-1.15, 1.15, 100)
        ax[1].plot(xa, pot2(xa, vc),   color='maroon',   label='V(x)=c$x^2$')
        ax[1].legend()
        ax[1].set_xlabel(r'$x$ [m]')
        ax[1].set_ylabel('V [J]')
        plt.show()
    if args.vall == True:
        fig,ax = plt.subplots(2,1, figsize=(10, 10) )

        # periodi
        ax[0].plot(a, T15,  color='forestgreen', label='V(x)=c$|x|^{3/2}$')
        ax[0].plot(a, T2,   color='red', label='V(x)=c$x^2$')
        ax[0].plot(a, T4,   color='royalblue', label='V(x)=c$x^4$')
        ax[0].plot(a, T6,   color='maroon',   label='V(x)=c$x^6$')
        ax[0].axhline(Tarm, color='tomato',    label='$2 \pi \sqrt{2c/m}$')
        ax[0].legend(loc='upper center', fontsize=13)
        ax[0].set_xlabel(r'$x_0$ [m]')
        ax[0].set_ylabel(r'T [s]')
        ax[0].set_ylim(0, 14)

        # subplot energia potenziale
        xa = np.linspace(-1.15, 1.15, 100)

        ax[1].plot(xa, pot(xa, vc),color='forestgreen',label='V(x)=c$|x|^{3/2}$')
        ax[1].plot(xa, pot2(xa, vc), color='red', label='V(x)=c$x^2$')
        ax[1].plot(xa, pot4(xa, vc), color='royalblue', label='V(x)=c$x^4$')
        ax[1].plot(xa, pot6(xa, vc), color='maroon',   label='V(x)=c$x^6$')
        ax[1].legend()
        ax[1].set_xlabel(r'$x$ [m]')
        ax[1].set_ylabel(r'V [J]')

        plt.show()

if __name__ == "__main__":
    oscillatore()
    
