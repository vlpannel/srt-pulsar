"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import psrdynspec
from psrdynspec import fold


class fold_blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Block to perform folding (without importing and using psrdynspec"""

    def __init__(self, period=.0335, samp_rate=1000000/32, integration_time=10.):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Fold',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[(np.float32, 1024)]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.period = float(period)
        self.samp_rate = float(samp_rate)
        self.integration_time = float(integration_time)
        
        self.bins = 1024
        self.profile = np.zeros(self.bins)
        self.data = np.array([], dtype=np.float32)
        
        self.fold_ts = fold.fold_ts

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        
        self.data = np.append(self.data, input_items[0])
        
        if self.data.size >= self.samp_rate * self.integration_time:
            times = np.arange(self.data.size) / self.samp_rate 
            self.profile = np.nan_to_num(fold.fold_ts(self.data, times, self.period, self.bins, True))[0]
            self.data = np.array([], dtype=np.float32)
            
        output_items[0][:] = np.array([self.profile] * output_items[0].shape[0])
        return len(output_items[0])
