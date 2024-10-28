import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("kplr010666592-2011240104155_slc.csv")
df_zoom=df.loc[( df['TIME'] < 940)& ( df['TIME'] > 939)]
ax=df_zoom["TIME"]
ay=df_zoom["SAP_FLUX"]
x=df["TIME"]
y=df["SAP_FLUX"]
fig, ax = plt.subplots(figsize=(12,6))
ins_ax = ax.inset_axes([1.10, 939.6,0.5 ,0.002 ]) # w.r.t. ax
ax.errorbar(x, y, yerr=df["SAP_FLUX_ERR"], fmt=".", color="darkgreen", markersize=10) 
ins_ax = ax.inset_axes([0.8, 0, 0.25, 0.2])  # Posizione e dimensioni relative all'area principale
ins_ax.errorbar(df_zoom["TIME"], df_zoom["SAP_FLUX"],  yerr=df_zoom["SAP_FLUX_ERR"], fmt=".", color="darkgreen")
ins_ax.set_xticklabels([]) #per togliere i valori dal mini grafico
ins_ax.set_yticklabels([])

plt.xlabel("TIME")
plt.ylabel("Sap_FLUX")
plt.title("grafico")

plt.show()


