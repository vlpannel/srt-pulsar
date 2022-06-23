import digital_rf
import datetime
import dateutil.parser
import calendar

import numpy as np
from matplotlib import pyplot as plt

# variables
top_lvl = '/Volumes/NO NAME/pulsar/2022-05-26/rf_data'	# top-level filepath for RF data
channel = 'misa-l2'	# channel to read from
pulsar_freq = 29.7	# frequency (Hz) of how often pulsar pulses
nsamp = 1000000	# number of samples to read

# read the data into a vector
do = digital_rf.DigitalRFReader(top_lvl)
try:
	assert channel in do.get_channels()
except AssertionError:
	print('Please set channel to an actual channel of this data.')
s, e = do.get_bounds(channel)
#nsamp = (e - s) / 2		# re-set number of samples based on bounds
prop = do.get_properties(channel)
samp_rate = prop['sample_rate_numerator'] / prop['sample_rate_denominator']
dvec = do.read_vector_c81d(s, nsamp, channel)

# split the data into channels by frequency (PFB)

# make a data set for each channel

# graph
dvec = dvec**2
plt.specgram(dvec, Fs=samp_rate)
plt.show()
