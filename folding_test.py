#!/usr/bin/env python
"""
Testing file for doing both PFB and folding (in separate functions).

Have not tested this code yet.

Takes raw data and puts it through PFB before folding and plotting pulsar data.
"""
import argparse
from pathlib import Path

import sys
import shutil
import math
import numpy as np
import digital_rf as drf
import matplotlib.pyplot as plt
from psrdynspec.modules.folding_plan import gen_octaves,  gen_periods, ProcessingPlan,update_processing_plan

#from gnuradio.filter import pfb
from mitarspysigproc import pfb, filtertools

from psrdynspec.modules.fold import execute_plan, fold_ts

def pfb():
    raw_data = "/Volumes/NO NAME/pulsar/2022-05-26/rf_data/"
    output_file = "/Users/vivelpanel/pfbdata/"  # this must exist before dw is created (this exists on current system now)
    secs = 120  # number of seconds to filter
    dr = drf.DigitalRFReader(raw_data)
    
    # do PFB on only one channel of raw_data (just for simplification)
    chan = do.get_channels()[0]
    props = dr.get_properties(chan)
    start = dr.get_bounds(chan)[0]
    data = dr.read_vector_c81d(start, props['samples_per_second']*secs, chan)
    
    out_chans = 31
    mask = [x for x in range(15)] + [y for y in range(17, 31)]
    pfb_data = pfb.pfb_decompose(data, out_chans, filtertools.kaiser_coeffs(out_chans), mask)
    
    dw = drf.DigitalRFWriter(output_file, np.complex64, secs, secs / 1000, 0, props['sample_rate_numerator'], props['sample_rate_denominator'], is_complex=True)
    dw.rf_write(data)
    

def fold_drf():
    data_path = "/Users/vivelpanel/pfbdata/"
    drfObj = drf.DigitalRFReader(data_path)
    chans = drfObj.get_channels()
    for ichan in chans:
        print('Folding Data from {0}'.format(ichan))
        bnds = drfObj.get_bounds(ichan)
        props = drfObj.get_properties(ichan)
        sr = props['samples_per_second']
        nsamps = sr*60*2#
        d1 = drfObj.read_vector(bnds[0], nsamps,ichan,0)
        times = np.arange(nsamps)/sr
        # crab pulsar period is same as folding period
        Nbins = 1024
        pfold = 33.5028583*1e-3
        profile, phibin_centers, counts = fold_ts(np.abs(d1)**2, times, pfold, Nbins, True)
        fig = plt.figure()
        plt.plot(phibin_centers,profile)
        plt.xlabel('phase')
        plt.ylabel('Counts')
        plt.title('Profile from {0} 2 minutes integration'.format(ichan))
        plt.grid(True)
        plt.savefig('{0}_profile.png'.format(ichan),dpi=300)


if __name__ == "__main__":
    pfb()
    fold_drf()

