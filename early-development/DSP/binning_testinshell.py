"""
This is a simply Python script to take in data and sort it into
bins before recombining the data. The point of this binning is to reduce the
noise in perceived signals.

WORK IN PROGRESS

Notes:
	- could combing all of this into a single function at some point
	- should probably adapt to deal with numpy vectors not lsts
"""

import random
import numpy as np

def main(num_bins, d):
	"""Assumes num_bins is an int showing how many bins data should be separated into and that data is a list."""
	bins = int(num_bins)
	data = d
	#debug_mode = False

	data = data[1:len(data) - 1]
	data = str.split(data)
	for i in range(len(data)):
		data[i] = int(data[i])

	sorted = []

	while bins > 0:
		items = random.randrange(1, len(data) - bins + 1)
		if bins == 1:
			items = len(data)
		
		sorted.append(data[:items])
		
		del data[:items]
		bins -= 1

	averaged = []
	for bin in sorted:
		averaged.append(sum(bin) / len(bin))

	print(sorted)

main(input('Num bins:\n\t'), input('Data (no commas):\n\t'))
