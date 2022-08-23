import numpy as np
import gnuradio
import digital_rf
import matplotlib.pyplot as plt

datapath = '/Users/vivelpanel/Desktop/sim_pfbdata/'
files = ['ch4', 'ch3', 'ch2', 'ch1']  # make sure files are in order from high to low freq
datatype = np.float32

stack = np.fromfile(open(datapath + files[0]), dtype=datatype)
for f in files[1:]:
    newdata = np.fromfile(open(datapath + f), dtype=datatype)
    newdata = np.append(newdata, [0] * (stack.shape[0] - newdata.shape[0]) )
    stack = np.vstack((stack, newdata))

print(stack[:][0:10])
plt.imshow(stack, aspect='auto')
plt.show()
