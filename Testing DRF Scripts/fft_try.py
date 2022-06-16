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

"""THIS CHUGS WAY TOO HARD"""

# fft
data = do.read_vector_c81d(s, spp * 60, chan)
fourier = np.fft.fft(data)
found_freqs = np.fft.fftfreq(data.size, d=int(do.get_properties(chan)['samples_per_second']))

# plot
plt.stem(found_freqs)
plt.show()
