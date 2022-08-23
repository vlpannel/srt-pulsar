"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

from psrdynspec.modules.fold import execute_plan, fold_ts

class blk(gr.sync_block):
    """
    Pulsar folding block - takes in time series of a single channel and folds it over the pulsar period.

    Outputs a vector of length Nbins which is the number of counts per phase bin (this can be used for plotting).

    
    Parameters
    ----------

    nsamps : int
        Number of samples coming in; the length of the vector passed in

    samp_rate : float
        Sample rate of data (taken from metadata)

    Nbins : int
        Number of phase bins in which to sort samples

    pfold : float
        Folding period (should be same or similar to period of pulsar)
    """

    def __init__(self, nsamps=int(120e6), samp_rate=32e3, Nbins=1024, pfold=33.5028583*1e-3):
        gr.sync_block.__init__(
            self,
            name='Pulsar Folding',   # will show up in GRC
            in_sig=[(np.complex64, nsamps)],
            out_sig=[(np.float32, Nbins), (np.float32, Nbins)]
        )
        '''
        Initializes pulsar folding block

        Parameters
        ----------

        nsamps : int
            Number of samples coming in-- the length of the vector passed in

        samp_rate : float
            Sample rate of data (taken from metadata)

        Nbins : int
            Number of phase bins in which to sort samples

        pfold : float
            Folding period (should be same or similar to period of pulsar)
        '''
        self.nsamps = nsamps
        self.samp_rate = samp_rate
        self.Nbins = Nbins
        self.pfold = pfold

        self.times = np.arange(nsamps)/samp_rate

    def work(self, input_items, output_items):

        # folding
        self.profile, self.phibin_centers, self.counts = fold_ts(np.abs(input_items[0])**2, self.times, self.pfold, self.Nbins, True)
        
        output_items[0] = self.times
        output_items[1] = self.profile
        return len(output_items[0])
