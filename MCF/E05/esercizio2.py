import numpy as np
import pandas as pd
import reco
import matplotlib.pyplot as plt
mod0df   = pd.read_csv("hit_times_M0.csv")
mod1df   = pd.read_csv("hit_times_M1.csv")
mod2df   = pd.read_csv("hit_times_M2.csv")
mod3df   = pd.read_csv("hit_times_M3.csv")
def mod0_to_hit():
    array=np.empty(0)
    for i,d in mod0df.iterrows():
        array=np.append(array, reco.Hit(modulo=d['mod_id'],sensore=d['det_id'],time_stamp=d['hit_time']))
    return array
def mod1_to_hit():
    array=np.empty(0)
    for i,d in mod1df.iterrows():
        array=np.append(array, reco.Hit(modulo=d['mod_id'],sensore=d['det_id'],time_stamp=d['hit_time']))
    return array
def mod2_to_hit():
    array=np.empty(0)
    for i,d in mod2df.iterrows():
        array=np.append(array, reco.Hit(modulo=d['mod_id'],sensore=d['det_id'],time_stamp=d['hit_time']))
    return array
def mod3_to_hit():
    array=np.empty(0)
    for i,d in mod3df.iterrows():
        array=np.append(array, reco.Hit(modulo=d['mod_id'],sensore=d['det_id'],time_stamp=d['hit_time']))
    return array
arrhit0=mod0_to_hit()
arrhit1=mod1_to_hit()
arrhit2=mod2_to_hit()
arrhit3=mod3_to_hit()
print(arrhit0)
