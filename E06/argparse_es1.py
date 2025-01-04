import sys,os
import argparse
from  scipy import integrate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def parse_arguments():
    
    parser = argparse.ArgumentParser(description='Esercizio 1:1 s vs t,2 v vs t',
                                     usage      ='python3 argparse_es1.py  --opzione')
    parser.add_argument('-v', '--vel',    action='store_true',                     help='grafico v vs t')
    parser.add_argument('-s', '--space',    action='store_true',                     help='grafico s vs t')
    
    return  parser.parse_args()


def main():
    dfvel=pd.read_csv('vel_vs_time.csv')
    args = parse_arguments()

    if args.vel == True:

        plt.plot(dfvel['t'],dfvel['v'], alpha=0.3, color='gold', label='velocità')
        plt.xlabel('tempo ',  fontsize=16)
        plt.ylabel('velocità',  fontsize=16)
        plt.legend(fontsize=14)
        plt.show()

    if args.space == True:
        dh=abs(dfvel['t'][1]-dfvel['t'][0])
        dist=[]
        for i in range(0,len(dfvel['t'])):
            s=integrate.simpson(dfvel['v'][0:i+1],dx=dh)
            dist.append(s)
        dist=np.array(dist)
        plt.plot(dfvel['t'],dist, alpha=0.3, color='gold', label='velocità')
        plt.xlabel('tempo ',  fontsize=16)
        plt.ylabel('velocità',  fontsize=16)
        plt.legend(fontsize=14)
        plt.show()



if __name__ == "__main__":

    main()
