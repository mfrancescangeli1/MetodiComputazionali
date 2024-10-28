import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("ExoplanetsPars_2024.csv",comment="#")
#print(df.columns)
#print(df.head)  stampa i primi valori/ultimi

x=df["st_mass"]
y=df["pl_orbper"]
plt.scatter(x,y)

plt.xlabel("massa")
plt.ylabel("Rmax")
plt.xscale('log')
plt.yscale('log')
plt.title("grafico")

plt.show()
