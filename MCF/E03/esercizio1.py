import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("kplr010666592-2011240104155_slc.csv")
x=df["TIME"]
y=df["SAP_FLUX"]
plt.rcParams["figure.figsize"]=[10,4.5]
plt.errorbar(x,y,yerr=df["SAP_FLUX_ERR"], marker=".", color="darkgreen", markersize=10)
plt.xlabel("TIME")
plt.ylabel("Sap_FLUX")
plt.title("grafico")
plt.savefig("kepler_es1.png")
plt.show()
