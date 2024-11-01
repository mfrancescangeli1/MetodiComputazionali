import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("kplr010666592-2011240104155_slc.csv")
df_zoom=df.loc[( df['TIME'] < 941)& ( df['TIME'] > 939)]
x=df_zoom["TIME"]
y=df_zoom["SAP_FLUX"]
plt.rcParams["figure.figsize"]=[10,4.5]
plt.errorbar(x,y,yerr=df_zoom["SAP_FLUX_ERR"], fmt=".", color="darkgreen", markersize=10)
plt.xlabel("TIME")
plt.ylabel("Sap_FLUX")
plt.title("grafico")
plt.savefig("kepler_es2.png")
plt.show()
