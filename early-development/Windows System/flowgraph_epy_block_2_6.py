import psrdynspec
from psrdynspec import fold as fld
import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self, sample_rate=1000000, nsamps=1000000, pfold=0.0335, Nbins=1024):
        gr.sync_block.__init__(
            self,
            name='Folding',
            in_sig=[(np.float32, nsamps)],
            out_sig=[(np.float32, Nbins)]
        )
        self.sample_rate = sample_rate
        self.nsamps = nsamps
        self.pfold = pfold
        self.Nbins = Nbins
        
        self.times = self.nsamps / self.sample_rate
        
        self.overall_fold = None
        
    def work(self, input_items, output_items):
        profile, phibin_centers, counts = fld.fold_ts(input_items[0][:], self.times, self.pfold, self.Nbins, return_counts=True)
        
        if self.overall_fold == None:
            self.overall_fold = profile
        else:
            self.overall_fold += profile
            
        output_items[0][:] = self.overall_fold