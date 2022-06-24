import digital_rf
import datetime
import dateutil.parser
import calendar

import numpy as np
from matplotlib import pyplot as plt
import scipy
from scipy import signal

# variables
top_lvl = '/Volumes/NO NAME/pulsar/2022-05-26/rf_data'	# top-level filepath for RF data
channel = 'misa-l2'	# channel to read from
pulsar_freq = 29.7	# frequency (Hz) of how often pulsar pulses
nsamp = 100000	# number of samples to read
center_freq = 440000000

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
nsamp = samp_rate * 3
dvec = do.read_vector_c81d(s + (samp_rate * 300), nsamp, channel)

# split the data into channels by frequency (PFB)


# make a data set for each channel


# graph
# This is using pyplot's specgram function to do all the work for me
plt.specgram(dvec, Fs=samp_rate, Fc=center_freq, NFFT=32768, noverlap=1024)
plt.show()
