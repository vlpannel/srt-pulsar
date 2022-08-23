import numpy as np
import matplotlib.pyplot as plt
from psrdynspec import fold as f

datafile = '/Users/vivelpanel/Desktop/vecfile'
data = np.fromfile(open(datafile))#[:int(.080584 * 5 * 1000000)]

nsamps = data.size
samp_rate = 1000000
Nbins = 1024
pfold = .080584

times = np.arange(nsamps) / samp_rate

profile, phibin_ctrs, counts = f.fold_ts(data, times, pfold, Nbins, True)

result = np.nan_to_num(profile)

plt.plot(result)
plt.show()
