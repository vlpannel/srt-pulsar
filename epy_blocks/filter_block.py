"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

import scipy
from scipy import stats

from collections import deque

class filter_outlier_block(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """
    Filter Outliers Block - passes data points through after replacing outliers with median value.

    Parameters
    ----------

    samp_rate : float, int
        Sample rate of incoming samples. Samples per second.

    time : float, int
        Amount of time to consider data. Seconds.

    deviations : int, float
        Number of deviations of variation from median that determines outlier.


    Notes
    -----

    Uses buffer of datapoints to calculate median and median absolute deviation. Outliers are points a number of deviations away from median (determined by parameter `deviation`). Size of buffer is numsamps where numsamps is the number of samples 
    """

    def __init__(self, samp_rate=(1000000/32), time=30, deviations=10):
        gr.sync_block.__init__(
            self,
            name='Filter Outliers',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.samp_rate = samp_rate
        self.time = time
        self.deviations = deviations

        self.buffer = np.array([], dtype=np.float32)   # buffer to contain data
        self.data = np.array([], dtype=np.float32)  # data to pass out
        self.median = 0.    # median of data in buffer
        self.mad = 0.   # median absolute deviation of data in buffer
        

    def work(self, input_items, output_items):
        numsamps = self.samp_rate * self.time   # number of samples to store in buffer
        if self.buffer.size < numsamps:
            self.buffer = np.append(self.buffer, input_items[0])
        else:
            self.buffer = np.append(np.delete(self.buffer, range(input_items[0].size)), input_items[0][:])
        if self.buffer.size > numsamps:
            self.buffer = np.delete(self.buffer, range(self.buffer.size - numsamps))

        self.data = input_items[0].copy()

        self.median = np.median(self.buffer)
        self.mad = scipy.stats.median_abs_deviation(self.buffer)

        self.data[np.where(np.absolute(self.data - self.median) > (self.deviations * self.mad))] = self.median
        
        output_items[0][:] = self.data[:]
        return len(output_items[0])

