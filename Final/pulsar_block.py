import numpy as np
from gnuradio import gr
import time

class blk(gr.sync_block):
    
    def __init__(self, period=.33, offset=0):
        gr.sync_block.__init__(
            self,
            name='Pulse Block',
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        self.start = time.time()
        self.per = period
        self.off = offset
    
    def work(self, input_items, output_items):
        now = time.time()
        pulse_flag = ((now - self.start - self.off) % self.per) <= .015
        output_items[0][:] = input_items[0] * pulse_flag
        return len(output_items[0])
