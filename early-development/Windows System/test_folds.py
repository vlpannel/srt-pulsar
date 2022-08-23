import numpy as np
import psrdynspec
from psrdynspec import fold as fld
import sys
import matplotlib.pyplot as plt
import matplotlib.colors as c

datadir = 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\'
files = ['ch' + str(n) for n in range(31)]#files = sys.argv[1:]
files = files[16:] + files[:16]
sr = 1000000.
per = .0335028583
Nbins = 1024
increment = 0

alldata = []

for f in files:
    print(f'folding {f}...')
    data = np.fromfile(datadir + f, dtype=np.complex64)
    folded = fld.fold_ts(np.absolute(data)**2, np.arange(data.size) * (1./sr), per, Nbins, True)
    #plt.plot(folded[0] + increment)
    #increment += 2
    #alldata += [np.absolute(data)**2]
    plt.plot(folded[0])
    plt.show()

'''
alldata = np.array(alldata)
print(f'DEBUG: data is {alldata}, size {alldata.shape}')
plt.imshow(alldata, aspect='auto')
'''

'''
plt.xscale('linear')
plt.yscale('linear')
'''
#plt.show()

