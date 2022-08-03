"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import digital_rf as drf

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, datadir='C:\\Users\\vlpannel\\Desktop\\raw', chan='ch0'):
        gr.sync_block.__init__(
            self,
            name='DRF Read Entire Channel',   # will show up in GRC
            in_sig=[],
            out_sig=[(np.complex64, 200)]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.datadir = datadir
        self.chan = chan

        self.drf_obj = drf.DigitalRFReader(self.datadir)
        self.s, self.e = self.drf_obj.get_bounds(self.chan)

        self.data = None
        
    def work(self, input_items, output_items):

        self.data = self.drf_obj.read_vector(self.s, 200, self.chan)
        self.s += 200
        
        output_items[0] = np.copy(self.data)
        return len(output_items[0])
