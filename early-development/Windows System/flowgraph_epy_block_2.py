import psrdynspec
from psrdynspec import fold as fld
import numpy as np
from gnuradio import gr
import matplotlib.pyplot as plt

class blk(gr.sync_block):
    def __init__(self, sample_rate=1000000.0, nsamps=8192, pfold=0.0335, Nbins=1024):
        gr.sync_block.__init__(
            self,
            name='Folding',
            in_sig=[(np.float32, 8192)],
            out_sig=[(np.float32, Nbins)]
        )
        self.sample_rate = sample_rate
        self.nsamps = nsamps
        self.pfold = pfold
        self.Nbins = Nbins
        
        self.times = np.arange(self.nsamps) / 8192.
        
        self.overall_fold = np.zeros(self.Nbins)
        
    def work(self, input_items, output_items):
        
        print(f'DEBUG: passed in was {input_items[0]} of size {input_items[0].size}')
        print(f'DEBUG: times is {self.times}')
        print(f'DEBUG: time series is {input_items[0][:]}')
        
        profile, phibin_centers, counts = fld.fold_ts(input_items[0][:], self.times, self.pfold, self.Nbins, return_counts=True)
        
        self.overall_fold += profile
        self.times += max(self.times) + self.times[1]
            
        output_items[0][:] = profile