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

def __init__(self, num_bins, data):
	"""Assumes num_bins is an int showing how many bins data should be separated into and that data is a list."""
	self.bins = num_bins
	self.data = data
	self.debug_mode = false

def sort(self):
	self.sorted = []
	data = self.data
	bins = self.bins
	
	while bins > 0:
		items = random.randrange(1, len(data) - bins + 1)
		if bins == 1:
			items = len(data)
		
		self.sorted.append(data[:items])
		
		del data[:items]
		bins -= 1

def take_averages(self):
	self.averaged = []
	for bin in self.sorted:
		self.averaged.append(sum(bin) / len(bin))

def main(self):
	self.sort(self)
	self.take_averages(self)
		
