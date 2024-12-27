import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("ExoplanetsPars_2024.csv",comment="#")
print(df.columns)
print(df.head)
transit_df=df.loc[df["discoverymethod"]=="Transit"]
radial_df=df.loc[df["discoverymethod"]=="Radial Velocity"]
fig,ax=plt.subplots(figsize=(8,6))
##massa del pianeta in funzione del periodo orbitale
plt.scatter(df['pl_orbper'],df['pl_bmassj'],
            alpha=0.3, color='forestgreen', label='Exoplanets')
plt.xlabel('Periodo')
plt.ylabel(r'massa pianeta')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
##plot Rmax2/m* in funzione del periodo orbitale
plt.scatter(df['pl_orbper'],(df['pl_orbsmax']**2)/df['st_mass'],
            alpha=0.3, color='forestgreen', label='Exoplanets')
plt.xlabel('Periodo')
plt.ylabel(r'(Planet Mass)$^2$/ [$m_*$]')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
##scatter distinzione per scoperta
plt.scatter(transit_df['pl_bmassj'],transit_df['pl_orbper'],
            c='red',label='transit discoveries')
plt.scatter(radial_df['pl_bmassj'],radial_df['pl_orbper'],
            c='green',label='radial velocity')
plt.xlabel("periodo orbitale")
plt.ylabel("massa")
plt.xscale('log')
plt.yscale('log')
plt.title("confronto massa-periodo orbitale, con distinzione per scoperta")
plt.legend()
plt.show()
##istogramma
plt.hist(transit_df['pl_orbper'], bins=50,
         color='red',  alpha=0.5, label='Transit')

plt.hist(radial_df['pl_orbper'],bins=50,
         color='green',  alpha=0.5, label='Radial Velocity')
plt.ylabel(r'Number of planets')
plt.legend()
plt.show()
##istogramma log10
plt.hist(np.log10(transit_df['pl_orbper']), bins=50,
         color='red',  alpha=0.5, label='Transit')

plt.hist(np.log10(radial_df['pl_orbper']),bins=50,
         color='green',  alpha=0.5, label='Radial Velocity')
plt.ylabel(r'Number of planets')
plt.legend()
plt.show()
##esercizio 2A

fig = plt.figure(figsize=(8,6)) 
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
ax = gs.subplots( sharex='col', sharey='row')
ax[0,0].hist( np.log10(transit_df[ 'pl_orbper']),
              bins=50,  color='red',  alpha=0.5, label='Transit')

ax[0,0].hist( np.log10(radial_df['pl_orbper']),
              bins=50, color='green',  alpha=0.5, label='Radial Velocity')
ax[0,0].set_ylabel(r'Number of planets')
ax[0,0].legend()
ax[1,0].scatter(np.log10(transit_df['pl_orbper']),
                np.log10(transit_df['pl_bmassj']),
                color='red',  alpha=0.4, label='Transit')
ax[1,0].scatter( np.log10(radial_df['pl_orbper']),
                 np.log10(radial_df['pl_bmassj']),
                 color='green', alpha=0.3, label='Radial Velocity')
ax[1,0].set_xlabel('log(Period [days])')
ax[1,0].set_ylabel(r'log(Planet Mass [$m_*$])')
ax[1,0].legend()

ax[1,1].hist( np.log10(transit_df['pl_bmassj']),bins=50, color='red',
              alpha=0.5, orientation='horizontal', label='Transit')
ax[1,1].hist( np.log10(radial_df['pl_bmassj']), bins=50, color='green',
              alpha=0.5, orientation='horizontal', label='Radial Velocity')
ax[1,1].set_xlabel( 'Number of planets')
ax[1,1].legend()
ax[0,1].axis('off')

plt.savefig('Exoplanets_Period_vs_Mass_Detection.pdf')
plt.savefig('Exoplanets_Period_vs_Mass_Detection.png')
plt.show()
