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

    def __init__(self, sr=1000000, per=.033):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Pulse',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.sr = sr    # sample rate
        self.per = per    # period of pulse
        self.counter = 0    # counting how many
        self.reset = (self.per + (.1 * self.sr))

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        if self.counter > self.reset:
            self.counter = 0
        
        if self.counter < self.per:
            output_items[0][:] = 0
        elif self.counter < reset:
            output_items[0][:] = input_items
        
        self.counter += 1
        
        return len(output_items[0])
