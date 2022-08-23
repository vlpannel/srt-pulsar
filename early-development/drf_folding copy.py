#!/usr/bin/env python
"""

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

from psrdynspec.modules.fold import execute_plan, fold_ts
def fold_drf():
    data_path = "/Users/swoboj/DATA/pulsar/pfbdata/"
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
        # crab pulsar period is .03362
        # metric_values, global_metricmax_index, global_metricmax, best_period, optimal_bins, optimal_dsfactor = execute_plan(d1, np.arange(nsamps), plan, 'reducedchisquare')
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

        plt.close(fig)
if __name__ == "__main__":
    fold_drf()
