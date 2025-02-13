#####################################################
#              Matteo Francescangeli                #
#     matteo.francescangeli1@studenti.unipg.it      #
#         Universià degli Studi di Perugia          #
#    Corso di Metodi Computazionali per la Fisica   #
#---------------------------------------------------#
#        Progetto: oscillazioni climatiche          #
#                                                   #
#####################################################

import sys, os
import numpy as np
import pandas as pd
from scipy import constants, fft, optimize
from scipy.signal import lombscargle, find_peaks
import matplotlib.pyplot  as plt
import scipy
import argparse
from astropy.timeseries import LombScargle

#Funzione per fit Spettro di Potenza del rumore         
def func(freq,k,beta):
    """
    Funzione per fit spettro potenza caratteristico del rumore
    freq: frequenze
    k: normalizzazione
    beta : esponente per dipendenza da frequenza

    return N/f^beta
    """    
    return k*(1/(freq**beta))
#Funzione per scelta di lombscargle         
def spettro(tempi,data,scelta):
    """
    Calcola lo spettro di potenza di un segnale con la possibilità di
    scegliere tra SciPy o Astropy.
    tempi: array dei tempi (si presume non regolari)
    data: array dei dati relativi
    scelta: 1->scipy 2->astropy

    return
    freq: array delle frequenze
    power: array delle potenze relative alle frequenze
    """
    freq=np.array([])
    power=np.array([])
    if len(tempi)==len(data):
        if scelta=='1':
            freq=np.linspace(1/np.max(np.abs(tempi)),
                             len(tempi)/(2*np.max(np.abs(tempi))),5000)
            w = 2 * np.pi * freq
            power=lombscargle(tempi, data, w,normalize=True)
        elif scelta=='2':
            ls = LombScargle(tempi, data)
            freq, power = ls.autopower()
    else:
        raise ValueError("Errore: 'tempi' e 'data' lunghezza diversa")
    return freq, power

#####################################################################
#      Funzione per gestione opzioni (argparse)                     #
#####################################################################

def parse_arguments():

    parser = argparse.ArgumentParser(description='oscillazioni climatiche',
                                     usage      ='python3 prova3.py  --option')
    parser.add_argument('--pt1',   action='store_true',
                        help='grafici di temperatura e concentrazione di CO2 rispetto al tempo')
    parser.add_argument('--pt2',  action='store_true',  
                        help='analisi di distanze temporali di campionamento')
    parser.add_argument('--pt3',    action='store_true',
                        help='Lombscargle e spettri di potenza')
    parser.add_argument('--pt4',     action='store_true',
                        help='fit degli spettri di potenza')
    parser.add_argument('--pt5',     action='store_true',
                        help='confronto nel dominio temporale e di frequenze')
    parser.add_argument('--pt6',     action='store_true',
                        help='individuazione frequenze principali')
    return  parser.parse_args(args=None if sys.argv[1:] else ['--help'])



#####################################################################
#             Funzione principale per calcolo FFT                   #         
#####################################################################

def main():
    args = parse_arguments()

    #-------------------------------------------------------------------------#
    #  Lettura files di dati (con controllo se sono presenti nella cartella)  #
    #-------------------------------------------------------------------------#
    if os.path.exists('edc3deuttemp2007-noaa.txt'):
        ttemp=pd.read_csv('edc3deuttemp2007-noaa.txt',comment='#',sep='\t')
    else:
        ttemp=pd.read_csv('https://www.ncei.noaa.gov/pub/data/paleo/icecore/antarctica/epica_domec/edc3deuttemp2007-noaa.txt',comment='#',sep='\t')
    if os.path.exists('edc3deuttemp2007-noaa.txt'):
        CO2=pd.read_csv('edc3-composite-co2-2008-noaa.txt',comment='#',sep='\t')
    else:
        CO2=pd.read_csv('https://www.ncei.noaa.gov/pub/data/paleo/icecore/antarctica/epica_domec/edc3-composite-co2-2008-noaa.txt',comment='#',sep='\t')
    
    
    #temperatura relativa alla variazione degli ultimi 1000 anni
    temp=ttemp.iloc[13:].reset_index(drop=True)
    CO2=CO2.astype({'CO2': 'float64'})
    #CO2 relativa alla variazione degli ultimi 1000 anni
    CO2_rel=CO2['CO2']-np.mean(CO2['CO2'][0:11])
    #definizione del tempo rispetto al presente
    yt=1950-temp['age_calBP']
    yc=2008-CO2['gas_ageBP']
    

    #---------------------------------------------------------------#
    #           Grafico temperatura e concentrazione di CO2         #
    #---------------------------------------------------------------#
    if args.pt1 == True:
        #grafici singoli
        plt.figure(1)
        plt.plot(yt, temp['Temperature'], color='firebrick')
        plt.title("Andamento temperatura")
        plt.ylabel('Temperatura(°C)')
        plt.xlabel('t(year)')
        plt.grid(True)

        plt.figure(2)
        plt.plot(yc,CO2['CO2'],color='blueviolet')
        plt.title(r"Andamento concentrazione di CO$_2$")
        plt.ylabel(r'concentrazione di CO$_2$(p.p.m)')
        plt.xlabel('t(year)')
        plt.grid(True)
        plt.show()
        fig, axs = plt.subplots(2, 1,layout="constrained")
        axs[0].plot(yt,temp['Temperature'],color='firebrick',alpha=0.7)
        axs[0].set_title("andamento temperatura")
        axs[0].set_ylabel('T(°C)')
        axs[0].set_xlabel('t(year)')
        axs[0].grid(True)
        axs[1].plot(yc,CO2_rel,color='blueviolet',alpha=0.7)
        axs[1].set_title(r"andamento concentrazione C$O_2$")
        axs[1].set_xlabel('t(year)')
        axs[1].set_ylabel(r'concentrazione di CO$_2$(p.p.m)')
        axs[1].grid(True)
        plt.show()
    #---------------------------------------------------------------#
    #                analisi distanze temporali                     #
    #---------------------------------------------------------------#
    if args.pt2==True:
        difft = []
        for i in range(len(yt) - 1):
            diff = yt[i] - yt[i+1]
            difft.append(diff)
        diffc = []
        for i in range(len(yc) - 1):
            diff = yc[i] - yc[i+1]
            diffc.append(diff)
         
        xt = np.arange(len(difft))
        xc = np.arange(len(diffc))
        fig, axs = plt.subplots(2, 1,layout="constrained")
        axs[0].scatter(xt,difft,color='maroon', label='dt (temperatura)',
                       marker='.',alpha=0.5)
        axs[0].set_ylabel('tempo (anni)')
        axs[0].set_xlabel('indice yt')
        axs[1].scatter(xc,diffc,color='blueviolet',label=r'dt (CO$_2$)',
                       marker='.',alpha=0.5)
        axs[1].set_ylabel('tempo (anni)')
        axs[1].set_xlabel('indice yc')
        axs[0].legend()
        axs[1].legend()
        plt.show()


    #---------------------------------------------------------------#
    #              Calcolo FFT e spettro di potenza                 #
    #---------------------------------------------------------------#
    if  args.pt3==True or args.pt4==True or args.pt5==True:
        scelta=input('sciegliere come calcolare lo spettro di potenza:\n 1)scipy \n 2) astropy \n')

        # Controllo di validità
        while scelta not in ['1', '2']:
            print("Errore: selezionare 1 (SciPy) o 2 (Astropy).")
            scelta = input('Scegliere come calcolare lo spettro di potenza:\n 1) SciPy \n 2) Astropy \n')
            print(f"Hai scelto l'opzione {scelta}")
        #-----------------------------------------------------------#
        #          Calcolo spettro di potenze con LombScargle       #
        #-----------------------------------------------------------#
        freqt, powert=spettro(yt,temp['Temperature'],scelta)
        freqc, powerc=spettro(yc,CO2_rel,scelta)
        
        
        #---------------------------------------------------------------#
        #           Grafico spettro di potenza (scala log)              #
        #---------------------------------------------------------------#
        if args.pt3 == True:

           fig, axs = plt.subplots(2, 1,layout="constrained")
           axs[0].plot(freqt,powert,color='maroon', label='temperatura',
                       alpha=0.7)
           axs[0].scatter(freqt,powert,marker='.',color='darkred',
                          label='temperatura',alpha=0.3)
           axs[0].set_title("spettro di potenza")
           axs[0].set_ylabel(r'$\left| c_k \right|^2$')
           axs[0].set_xlabel('frequenza(1/yr)')
           axs[0].set_xscale('log')
           axs[0].set_yscale('log')
           axs[0].legend()
           axs[0].grid(True)
           axs[1].plot(freqc,powerc,color='indigo',
                       label=r'concentrazione C$O_2$',alpha=0.7)
           axs[1].scatter(freqc,powerc,marker='.',color='indigo',
                          label=r'concentrazione C$O_2$',alpha=0.3)
           axs[1].set_xlabel('frequenza(1/yr)')
           axs[1].set_ylabel(r'$\left| c_k \right|^2$')
           axs[1].set_xscale('log')
           axs[1].set_yscale('log')
           axs[1].legend()
           axs[1].grid(True)
           plt.show()
           r'''
        #---------------------------------------------------------------#
        #           Grafico spettro di potenza periodicità              #
        #---------------------------------------------------------------#
           fig, axs = plt.subplots(2, 1,layout="constrained")
           axs[0].plot(1/freqt[1:],powert[1:],marker='.',label='temperatura',
                       color='maroon',alpha=0.7)
           axs[0].set_title("spettro di potenza su periodo")
           axs[0].set_ylabel(r'$\left| c_k \right|^2$')
           axs[0].set_xlabel('periodo (yr)')
           axs[0].grid(True)
           axs[1].plot(1/freqc[1:],powerc,marker='.',
                       label=r'concentrazione di C$O_2$',
                       color='indigo',alpha=0.7)
           axs[1].set_xlabel('periodo (yr)')
           axs[1].set_ylabel(r'$\left| c_k \right|^2$')
           axs[1].grid(True)
           plt.show()
        '''
           #---------------------------------------------------------------#
           #           Grafico spettro di potenza periodicità (log)        #
           #---------------------------------------------------------------#
           fig, axs = plt.subplots(2, 1,layout="constrained")
           axs[0].plot(1/freqt[1:],powert[1:],color='maroon',
                       label='temperatura',alpha=0.7)
           axs[0].scatter(1/freqt[1:],powert[1:],
                          marker='.',color='maroon',alpha=0.3)
           axs[0].set_title("spettro di potenza su periodo")
           axs[0].set_ylabel(r'$\left| c_k \right|^2$')
           axs[0].set_xlabel('periodo (yr)')
           axs[0].set_xscale('log')
           axs[0].set_yscale('log')
           axs[0].legend()
           axs[0].grid(True)
           axs[1].scatter(1/freqc[1:],powerc[1:],marker='.',color='blueviolet',
                          label=r'concentrazione di C$O_2$',alpha=0.3)
           axs[1].plot(1/freqc[1:],powerc[1:],
                       color='blueviolet',alpha=0.7)
           axs[1].set_xlabel('periodo (yr)')
           axs[1].set_ylabel(r'$\left| c_k \right|^2$')
           axs[1].set_xscale('log')
           axs[1].set_yscale('log')
           axs[1].legend()
           axs[1].grid(True)
           plt.show()

        #---------------------------------------------------------------#
        #                   Fit spettro di potenza                      #
        #---------------------------------------------------------------#

        if args.pt4 == True:
            #considerando tutto l'array dei tempi
            pt, ptc=scipy.optimize.curve_fit(func,freqt,powert, p0=[1e-5, 2])
            pc, pcc=scipy.optimize.curve_fit(func,freqc,powerc, p0=[1e-5, 0])
            #escludendo le frequenze più alte (più soggette a rumore)
            maskt = (freqt<0.003)
            maskc = (freqc<0.003)
            freqt1=freqt[maskt]
            powert1=powert[maskt]
            freqc1=freqc[maskc]
            powerc1=powerc[maskc]
            pt1, ptc1=scipy.optimize.curve_fit(func,freqt1,powert1,p0=[1e-5, 2])
            pc1, pcc1=scipy.optimize.curve_fit(func,freqc1,powerc1,p0=[1e-5, 0])
            
            #escludendo le frequenze con maggiore potenza
            #(osservazione empirica)
            masktf =  (freqt1 < 6.24e-6) | (freqt1 > 4.50e-5)
            maskcf = (freqc1 < 4.12e-6) | (freqc1 > 4.38e-5)
            mt=np.logical_not(masktf)
            mc=np.logical_not(maskcf)
            freqt2=freqt1[masktf]
            powert2=powert1[masktf]
            freqc2=freqc1[maskcf]
            powerc2=powerc1[maskcf]

            pt2, ptc2=scipy.optimize.curve_fit(func,freqt2,powert2,p0=[1e-5, 1])
            pc2, pcc2=scipy.optimize.curve_fit(func,freqc2,powerc2,p0=[1e-5, 1])
            ##grafico dei risultati di fit
            #primo fit
            fig, axs = plt.subplots(2, 1,layout="constrained")
            axs[0].plot(freqt[1:],powert[1:],color='maroon',label='temperatura')
            axs[0].plot(freqt[1:],func(freqt[1:],pt[0],pt[1]),
                        color='darkgreen', label='fit0')
            axs[0].set_xlabel('Frequenza [1/yr]')
            axs[0].set_ylabel(r'$\left| c_k \right|^2$')
            axs[0].set_xscale('log')
            axs[0].set_yscale('log')
            axs[0].legend(loc='lower left')
            axs[1].plot(freqc[1:],powerc[1:],color='blueviolet',label=r'CO$_2$')
            axs[1].plot(freqc[1:],func(freqc[1:],pc[0],pc[1]),
                        color='goldenrod', label='fit0')
            axs[1].set_xlabel('Frequenza [1/yr]')
            axs[1].set_ylabel(r'$\left| c_k \right|^2$')
            axs[1].set_xscale('log')
            axs[1].set_yscale('log')
            axs[1].legend(loc='lower left')
            plt.show()
            #secondo fit
            fig, axs = plt.subplots(2, 1, layout='constrained')
            axs[0].plot(freqt1,powert1,color='maroon',alpha=0.7)
            axs[0].scatter(freqt1[mt],powert1[mt],color='red',alpha=0.7)
            axs[0].plot(freqt1,func(freqt1,pt2[0],pt2[1]),color='darkgreen',
                        label='fit 2')
            axs[0].set_xlabel('Freq. [Hz]')
            axs[0].set_ylabel(r'$\left| c_k \right|^2$')
            axs[0].set_xscale('log')
            axs[0].set_yscale('log')
            axs[0].legend(loc='lower left')
            axs[1].plot(freqc1,powerc1,color='blueviolet',alpha=0.7)
            axs[1].scatter(freqc1[mc],powerc1[mc],color='red',alpha=0.7)
            axs[1].plot(freqc2,func(freqc2,pc2[0],pc2[1]),color='goldenrod',
                        label='fit 2')
            axs[1].set_xlabel('Freq. [Hz]')
            axs[1].set_ylabel(r'$\left| c_k \right|^2$')
            axs[1].set_xscale('log')
            axs[1].set_yscale('log')
            axs[1].legend(loc='lower left')
            plt.show()
            print(f"pt1: {pt1}, pt2: {pt2}")
            print(f"pc1: {pc1}, pc2: {pc2}")
           
        if args.pt5:
            # Sovrapposizione grafica dominio temporale
            t_norm=(temp['Temperature']-np.min(temp['Temperature']))/(np.max(temp['Temperature'])-np.min(temp['Temperature']))
            c_norm=(CO2_rel-np.min(CO2_rel))/(np.max(CO2_rel)-np.min(CO2_rel))
            plt.figure(figsize=(10, 6))
            plt.plot(yt, t_norm,label='Temperatura Normalizzata',
                         color='firebrick',alpha=0.6)
            plt.plot(yc, c_norm, label='CO2 Normalizzata',
                         color='blueviolet',alpha=0.6)
            plt.xlabel('tempo (year)')
            plt.ylabel('Valore Normalizzato (0-1)')
            plt.title('Andamento normalizzato Temperatura e CO2 (Min-Max)')
            plt.legend()
            plt.grid()
            plt.show()
            #dominio di frequenze
            lst_norm=LombScargle(yt,t_norm)
            lsc_norm=LombScargle(yc,c_norm)
            freqtn, powertn = lst_norm.autopower()
            freqcn, powercn = lsc_norm.autopower()
            plt.plot(freqtn,powertn,color='maroon',alpha=0.3)
            plt.scatter(freqtn,powertn,marker='+',color='maroon',alpha=0.4)
            plt.plot(freqcn,powercn,color='indigo',alpha=0.3)
            plt.scatter(freqcn,powercn,marker='.',color='indigo',alpha=0.4)
            plt.title("confronto spettro di potenza (normalizzato)")
            plt.xscale('log')
            plt.yscale('log')
            plt.xlabel('frequenza(1/yr)')
            plt.grid(True)
            plt.show()
            
    if args.pt6:
        #l'analisi è stata fatta con LombScargle di Astropy per sfruttarne le
        #informazioni aggiuntive
        
        lst = LombScargle(yt, temp['Temperature'])
        freqt, powert = lst.autopower()
        lsc= LombScargle(yc,CO2_rel)
        freqc, powerc = lsc.autopower()
        #escludendo le frequenze più alte (più soggette a rumore)
        maskt = (freqt<0.003)
        maskc = (freqc<0.003)
        freqt1=freqt[maskt]
        powert1=powert[maskt]
        freqc1=freqc[maskc]
        powerc1=powerc[maskc]

        #escludendo le frequenze con maggiore potenza
        masktf =  (freqt1 < 4.12e-6) | (freqt1 > 4.38e-5)
        maskcf = (freqc1 < 4.12e-6) | (freqc1 > 4.38e-5)
        freqt2=freqt1[masktf]
        powert2=powert1[masktf]
        freqc2=freqc1[maskcf]
        powerc2=powerc1[maskcf]

        #pt2, ptc2=scipy.optimize.curve_fit(func,freqt2,powert2,p0=[1e-5, 1])
        #pc2, pcc2=scipy.optimize.curve_fit(func,freqc2,powerc2,p0=[1e-5, 1])
        mt=np.logical_not(masktf)
        mc=np.logical_not(maskcf)
        ##grafico dei frequenze principali
        # fit
        peakst, _ = find_peaks(powert1, height=1e-2, prominence=0.05)
        peaksc, _ = find_peaks(powerc1, height=1e-2, prominence=0.07)
        fig, axs = plt.subplots(2, 1, layout='constrained')
        axs[0].plot(freqt1,powert1,color='maroon',alpha=0.7)
        axs[0].scatter(freqt1[mt],powert1[mt],color='red',alpha=0.7,
                       label='punti esclusi dal fit')
        axs[0].scatter(freqt1[peakst],powert1[peakst],
                       color='gold',label='picchi')
        axs[0].set_xlabel('Freq. [Hz]')
        axs[0].set_ylabel(r'$\left| c_k \right|^2$')
        axs[0].set_xscale('log')
        axs[0].set_yscale('log')
        axs[0].legend(loc='lower left')
        axs[1].plot(freqc1,powerc1,color='blueviolet',alpha=0.7)
        axs[1].scatter(freqc1[mc],powerc1[mc],color='red',alpha=0.7,
                       label='punti esclusi dal fit')
        axs[1].scatter(freqc1[peaksc],powerc1[peaksc],
                       color='gold',label='picchi')
        axs[1].set_xlabel('Freq. [Hz]')
        axs[1].set_ylabel(r'$\left| c_k \right|^2$')
        axs[1].set_xscale('log')
        axs[1].set_yscale('log')
        axs[1].legend(loc='lower left')
        plt.show()

        # Frequenze corrispondenti ai picchi
        peak_freqt = freqt[peakst]  
        peak_freqc = freqc[peaksc]  
        #ricostruzione segnale
        tempf = np.zeros_like(yt, dtype=float)
        for f in peak_freqt:
            tempf += lst.model(yt, f)
        plt.plot(yt, temp['Temperature'], label="Segnale originale")
        plt.plot(yt, tempf, label="Segnale ricostruito", linestyle="--")
        plt.xlabel("Tempo")
        plt.ylabel("Ampiezza")
        plt.legend()
        plt.title("Ricostruzione del segnale  dalle frequenze principali")
        plt.show()
        #ricostruzione segnale
        CO2f = np.zeros_like(yc,  dtype=float)
        for f in peak_freqc:
            CO2f += lsc.model(yc, f)
            
        plt.plot(yc, CO2_rel, label="Segnale originale")
        plt.plot(yc, CO2f, label="Segnale ricostruito", linestyle="--")
        plt.xlabel("Tempo")
        plt.ylabel("Ampiezza")
        plt.legend()
        plt.title("Ricostruzione del segnale dalle frequenze principali")
        plt.show()
        # Stampa delle frequenze principali
        print("Frequenze principali  della temperatura:")
        for f in peak_freqt:
            print("frequenza=",f," 1/yr --->periodicità= ", 1/f,"\n") 
        print(r"Frequenze principali  dell'andamento di CO2:")
        for f in peak_freqc:
            print("frequenza=",f," 1/yr --->periodicità= ", 1/f,"\n") 
            
            

if __name__ == "__main__":
    main()
