"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import time

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, period=.33, offset=0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Pulsing',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.period = period
        self.offset = offset
        self.s = time.time()		# note: I'm pretty sure start is a reserved keyword!

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        pulse_flag = ((time.time() - self.s - self.offset) % self.period) <= .015
        output_items[0][:] = input_items[0] * int(pulse_flag)
        return len(output_items[0])
