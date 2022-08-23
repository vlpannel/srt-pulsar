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
import collections


class filter_outlier_blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, samp_rate=1000000/32, time=30, deviations=10):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Filter Outliers',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.samp_rate = samp_rate
        self.time = time
        self.deviations = deviations
        
        self.buffer = collections.deque([])
        self.data = np.array([], dtype=np.float32)
        self.median = 0.
        self.mad = 0.

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        nsamps = self.samp_rate * self.time
        self.buffer.extend(input_items[0])
        while len(self.buffer) > nsamps:
            self.buffer.popleft()
        '''
        if len(self.buffer) < nsamps:
            self.buffer.extend(input_items[0])
        else:
            self.buffer.extend(np.delete(self.buffer, range(input_items[0].size)), input_items[0][:])
        if self.buffer.size > nsamps:
            self.buffer = np.delete(self.buffer, range(self.buffer.size - nsamps))
        '''
            
        self.data = input_items[0].copy()
        
        self.median = np.median(self.buffer)
        self.mad = scipy.stats.median_abs_deviation(self.buffer)
        
        self.data[np.where(np.absolute(self.data - self.median) > (self.deviations * self.mad))] = self.median
        
        output_items[0][:] = self.data[:]
        return len(output_items[0])
