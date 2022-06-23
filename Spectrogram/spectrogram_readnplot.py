#!/usr/bin/env python3

import os
import numpy as np
from matplotlib import pyplot as plt

# find and read all channel files
p = '/Users/vivelpanel/Desktop/SRT UROP 2022/Spectrogram/channels/'
files = os.listdir(path = p)
channel_data = []
for f in files:
	print(f"\n\n\nDEBUG #0:\n\tf = {f}\n\tp+f = {p + f}\n\tarray is {np.fromfile((p+f),dtype=np.complex64)}")
	channel_data.append(np.fromfile((p + f), dtype = np.complex64))

print(f"\n\n\nDEBUG #1:\n\tp = {p}\n\tfiles = {files}\n\tchannel_data = {channel_data}\n")

# find dimensions to plot
num_chan = len(files)
num_pts = channel_data[0].size	# assumes all channels are same size/number of samples and that all channels yield 1D data
x = num_chan * list(range(num_pts))
y = []
for i in range(num_chan):
	y += num_pts * [i]

print(f"DEBUG #2:\n\tnum_chan = {num_chan}\t\tnum_pts = {num_pts}\n\tx = {x}\t\ty = {y}")

# "weights" are amplitude of each freq
w = []
for set in channel_data:
	w.append(list(set))

print(f"DEBUG #3:\n\tw = {w}")

# plot on spectrogram
plt.hist2d(x, y, bins=[num_pts, num_chan], weights = w)
plt.show()
