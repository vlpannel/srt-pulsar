import digital_rf
import datetime
import dateutil.parser
import calendar
from matplotlib import pyplot as plt
import numpy as np
import random

# initialize DRF object, channel and start and end sample indices
do = digital_rf.DigitalRFReader('/Volumes/NO NAME/pulsar/2022-05-26/rf_data')
chan = 'misa-l2'
s,e = do.get_bounds(chan)

# find samples per second and per pulse
total_samps = (int)(do.get_properties(chan)['samples_per_second'])
spp = int(total_samps * .033 + .9999)

# 
# pnum = 1    # plot number (used for subplotting)
n = 3	    # number of times the start of folding is shifted
m = 1000	    # number of times folding over
p = 1	    # how many pulses wide a sample should be
for i in range(n):# sets various start points for folding
    s = int(do.get_bounds(chan)[0] + (spp * (i/(n + 1))))   # set the starting index of the first vector
    # s = random.randrange(s, e - 2 * m * p * spp)
    folded = np.zeros(p * spp)
    for j in range(m):	    # fold many times
        vec = do.read_vector_c81d(int(s + (j * p * spp)), p * spp, chan)
        mag = (vec.real * vec.real) + (vec.imag * vec.imag)
        folded = folded + mag

    folded = folded / m
    plt.subplot(n // 4 + 1, 4, i + 1)
    # pnum += 1
    # plt.figure()
    plt.plot(folded)

plt.show()
