"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, samp_rate=1000000, period=.033):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Pulse',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.samp_rate = samp_rate
        self.period = period
        self.counter = 0
        self.reset = self.period + 10

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        
        if self.counter > self.reset:
            self.counter = 0
        
        if self.counter > self.period:
            output_items[0][:] = input_items[0][:]
        else:
            output_items[0][:] = 0
        
        self.counter += len(output_items[0])
        
        if self.counter > self.reset:
            print('REPEAT')
        
        return len(output_items[0])
