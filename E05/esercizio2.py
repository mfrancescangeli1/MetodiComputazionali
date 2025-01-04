import numpy as np
import pandas as pd
import reco
import matplotlib.pyplot as plt
mod0df   = pd.read_csv("hit_times_M0.csv")
mod1df   = pd.read_csv("hit_times_M1.csv")
mod2df   = pd.read_csv("hit_times_M2.csv")
mod3df   = pd.read_csv("hit_times_M3.csv")
def get_hit(df):
    
    hit=np.array([reco.Hit(t['mod_id'], t['det_id'], t['hit_time'])
                  for i,t in df.iterrows()])
    return hit

arrhit0=get_hit(mod0df)
arrhit1=get_hit(mod1df)
arrhit2=get_hit(mod2df)
arrhit3=get_hit(mod3df)
hits=np.concatenate((arrhit0,arrhit1,arrhit2,arrhit3))
hits.sort()
#hit successivi
hit_dt=np.zeros(len(hits))
for i in range(0,len(hits)):
    hit_dt[i]=(hits[i]-hits[i-1]).astype(float)
mask=hit_dt>0
#scala lineare
plt.hist(np.log10(hit_dt[mask]), bins=100)
plt.xlabel("log(Delta_t) [ns]")
plt.show()
#scala logaritmica
logbins = np.logspace(0, 6, 100)
plt.hist(np.log10(hit_dt[mask]), bins=logbins)
plt.xlabel("Delta_t [ns]")
plt.xscale('log')
plt.yscale('log')
plt.show()
