#!/usr/bin/env python3

import os
import numpy as np
from matplotlib import pyplot as plt

# find and read all channel files
p = '/Users/vivelpanel/SRT UROP 2022/Spectrogram/channels/'
files = os.listdir(path = p)
channel_data = []
for f in files:
	channel_data.append(np.fromfile((p + f), dtype = np.complex64))

# find dimensions to plot
num_chan = len(files)
num_pts = len(channel_data[0].size)	# assumes all channels are same size/number of samples and that all channels yield 1D data
x = num_chan * list(range(num_pts))
y = []
for i in range(num_chan):
	y += num_pts * [i]

# "weights" are amplitude of each freq
w = []
for set in channel_data:
	w.append(list(set))

# plot on spectrogram
plt.hist2d(x, y, bins=[max(x), max(y)], weights = w)
plt.show()
