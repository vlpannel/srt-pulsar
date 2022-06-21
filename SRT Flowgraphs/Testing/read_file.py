#!/usr/bin/env python3

"""
This is just to test reading the binary files stored by GNU Radio's file sink block.
"""

import numpy
from matplotlib import pyplot as plt

filename = "/Users/vivelpanel/Desktop/SRT UROP 2022/SRT Flowgraphs/Testing Output Files/testbinary"
f = numpy.fromfile(filename, dtype = numpy.complex64)
print(f)    # should print a numpy array of complex64s
#print(f'TYPE: {type(f)} of size {f.size} (size is type {type(f.size)})')
print(range(f.size))

# NOTE: the file is a cosine wave w/ freq 1 kHz, amplitude 1, and sample rate 32 kHz

re = f.real
im = f.imag

plt.plot(re)
plt.plot(im)
plt.show()

plt.plot(re + im)
plt.show()
