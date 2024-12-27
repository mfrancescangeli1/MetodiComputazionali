import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("kplr010666592-2011240104155_slc.csv")
x=df["TIME"]
y=df["SAP_FLUX"]
plt.rcParams["figure.figsize"]=[10,4.5]
plt.errorbar(x,y,yerr=df["SAP_FLUX_ERR"], marker=".",
             color="darkgreen", markersize=10)
plt.xlabel("TIME")
plt.ylabel("Sap_FLUX")
plt.title("grafico")
#plt.savefig("kepler_es1.png")
plt.show()



###zoom su un picco
plt.subplots(figsize=(12,6))
plt.errorbar(df.loc[(df['TIME']> 950.25)&(df['TIME']< 950.43),'TIME'],
             df.loc[(df['TIME']> 950.25)&(df['TIME']< 950.43),'PDCSAP_FLUX'],
              yerr=df.loc[(df['TIME']> 950.25)&(df['TIME']< 950.43),
                              'PDCSAP_FLUX_ERR'], fmt='.',  color='maroon')

plt.xlabel('TIME', fontsize=14)
plt.ylabel(r'FLUX ($e^-/s$)',fontsize=14)
#plt.savefig('kepler_es1_zoom.png')
#plt.savefig('kepler_es1_zoom.pdf')
plt.show()


###con riquadro
fig, ax = plt.subplots(figsize=(12,6))
plt.errorbar(x,y,yerr=df["SAP_FLUX_ERR"], marker=".",
             color="darkgreen", markersize=10)
plt.xlabel("TIME")
plt.ylabel("Sap_FLUX")
plt.title("grafico")
ins_ax=ax.inset_axes([.65, .60, .32, .32])
ins_ax.errorbar(df.loc[(df['TIME']> 950.25)&(df['TIME']< 950.43),'TIME'],
             df.loc[(df['TIME']> 950.25)&(df['TIME']< 950.43),'PDCSAP_FLUX'],
              yerr=df.loc[(df['TIME']> 950.25)&(df['TIME']< 950.43),
                              'PDCSAP_FLUX_ERR'], fmt='.',  color='maroon')

plt.show()
