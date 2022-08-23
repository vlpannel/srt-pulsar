import numpy as np
from gnuradio import gr
import psrdynspec
from psrdynspec import fold
import pandas as pd
from astropy.stats import sigma_clip
from psrdynspec.modules.filters1d import blockavg1d

class fold_stream_block(gr.sync_block):
    """
    Fold a timeseries of power over a period.

    Parameters
    ----------
    
    per : float
        Period of folding
    
    samp_rate : float, int
        Sample rate of incoming samples.
        
    integration_time : int, float
        Seconds over which to integrate/fold.
        
    Nbins : int
        Number of phase bins to use for folding.
        
    folding : bool
        Flag determining whether new profiles are still being calculated
    
    Notes
    -----
    
    Outputs the profile resultant of the latest vector passed in.
    """

    def __init__(self, per=.1, samp_rate=1000, integration_time=.5, Nbins=1024, folding=True):
        
        '''
        @staticmethod
        def set_stuff(sr, it, bins):
            self.samp_rate = samp_rate
            self.integration_time = integration_time
            self.Nbins = bins
            
        set_stuff(samp_rate, integration_time, Nbins)
        '''
        
        gr.sync_block.__init__(
            self,
            name='Fold Stream',
            in_sig=[np.float32],
            out_sig=[]
        )
        self.per = per
        self.samp_rate = samp_rate
        self.integration_time = integration_time
        self.Nbins = Nbins
        self.folding = folding
        
        #self.start_time = 0
        self.data = []
        #self.ts = np.array([], dtype=np.float32)
        #self.times = np.array([], dtype=np.float32)
        #self.profile = np.zeros(self.Nbins, dtype=np.float32)

    def work(self, input_items, output_items):
        print(f'DEBUG: {input_items}\n\n\n\t{input_items[0]}')
        self.data += list(input_items[0])
        if len(self.data) >= int(self.samp_rate * self.integration_time):
            times = np.arange(len(self.data)) / float(self.samp_rate)
            folded = fold.fold_ts(self.data, times, self.per, self.Nbins)[0]
            print(folded)
            self.data = []
            
        return 0
        '''
        for vindex in range(len(input_items[0])):
            times = np.arange(input_items[0][vindex].size) / float(self.samp_rate) + self.start_time
            folded = fold.fold_ts(input_items[0][vindex], times, self.per, self.Nbins)[0]
            output_items[0][vindex] = folded
            self.start_time = times[1] + times[-1]
        self.start_time = 0
        return len(output_items[0])
        '''
        '''
        # if in folding mode and haven't yet collected enough data
        input0 = input_items[0]
        output0 = output_items[0]
        
        print(f'{input0}, {output0}')
        print(f'{self.folding}')
        print(f'{self.times >= self.integration_time}')
        print(f'{(self.folding) and not (True in self.times >= self.integration_time)}')
        
        if (self.folding) and not (True in self.times >= self.integration_time):
            print('DEBUG: folding...')
            self.ts = np.append(self.ts, input0[:])
            self.times = np.append(self.times, ( np.arange(len(input0))/float(self.samp_rate) ) + self.start_time)
            self.start_time = self.times[-1] + (1 / self.samp_rate)
            #print(f'\tts: {self.ts}\n\ttimes: {self.times}\n\tstart time: {self.start_time}')
        # reset if not folding or  enough data collected
        else:
            print('DEBUG: resetting...')
            self.start_time = 0
            self.profile = np.nan_to_num(fold.fold_ts(self.ts, self.times, self.per, self.Nbins)[0])
            self.ts = np.array([], dtype=np.float32)
            self.times = np.array([], dtype=np.float32)
            print(f'\tprofile: {self.profile}')
        # output profile vector
        for vecindex in range(len(output_items[0])):
            output_items[0][vecindex][:] = self.profile
        print(f'result shape: {output_items[0].shape}')
        return len(output_items[0])
        '''
