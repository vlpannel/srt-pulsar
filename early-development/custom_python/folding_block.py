import numpy as np
from gnuradio import gr
import psrdynspec
from psrdynspec import fold
from collections import deque

class fold_blk(gr.sync_block):
    """Block to perform folding (without importing but still [ab]using psrdynspec)"""

    def __init__(self, period=0.0333924123 , samp_rate=1000000/32, integration_time=10.):
        """
        Folding block - folds time series of power to find pulsars.

        Parameters
        ----------

        period : float
            Folding period

        samp_rate : float
            Sample rate of incoming samples

        integration_time : float
            Number of seconds over which to integrate
        
        Notes
        -----
        Always outputs the last calculated phase vs. power profile.

        After calculating, immediately begins collecting data for a new calculation.
        
        """
        gr.sync_block.__init__(
            self,
            name='Fold',
            in_sig=[np.float32],
            out_sig=[(np.float32, 1024)]    # 1024 bins; if needing more/fewer bins, must also manually change this
        )
        self.period = float(period)
        self.samp_rate = float(samp_rate)
        self.integration_time = float(integration_time)

        self.bins = 1024
        self.profile = np.zeros(self.bins)
        self.data = np.array([], dtype=np.float32)

        self.fold_ts = fold.fold_ts

    def work(self, input_items, output_items):

        # aggregate data
        self.data = np.append(self.data, input_items[0])

        # if enough data collected
        if self.data.size >= self.samp_rate * self.integration_time:
            times = np.arange(self.data.size) / self.samp_rate
            self.profile = np.nan_to_num(self.fold_ts(self.data, times, self.period, self.bins, True)[0])
            self.data = np.array([], dtype=np.float32)

        # always output the latest computed profile
        output_items[0][:] = np.array([self.profile] * output_items[0].shape[0])
        return len(output_items[0])

