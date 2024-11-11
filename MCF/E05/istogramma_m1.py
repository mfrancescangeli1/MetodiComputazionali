import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

mod0df   = pd.read_csv("hit_times_M0.csv")
diff_hit=np.ma.ediff1d(mod0df['hit_time'])
delta_t=np.log10(diff_hit)
n, bis, p = plt.hist(delta_t, bins=50, color='gold', alpha=0.7 )
plt.xlabel('valore estratto ', fontsize=16)

plt.show()

