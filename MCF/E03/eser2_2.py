import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("ExoplanetsPars_2024.csv",comment="#")
transit_df=df.loc[df["discoverymethod"]=="transit"]
radial_df=df.loc[df["discoverymethod"]=="Radial Velocity"]
fig,ax=plt.subplots(figsize=(12,8))

plt.scatter(tra,y)
#da finire foto 21/10
plt.xlabel("massa")
plt.ylabel("Rmax")
plt.xscale('log')
plt.yscale('log')
plt.title("confronto massa-periodo orbitale, con distinzione per scoperta")

plt.show()
