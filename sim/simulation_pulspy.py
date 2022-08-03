# this module will be imported in the into your flowgraph

import numpy as np

def pulsing_repeats(sr, ran):
    '''
    Parameters
    ----------

    sr : float
        Sample rate (determines frequencies that pulse goes over)

    ran : array-like, numpy array
        Range of values where frequency varies


    Returns
    -------

    repeats : array-like
        Number of samples at each frequency (before pulse moves to next frequency)
    '''

    # based on dispersion measure equation

    dm = .0127 # dispersion measure [pc*cm^-3]: arxiv.org/abs/2207.04267
    kdm = 4.149e18 # dispersion constant [Hz^2*pc^-1*cm^3*ms] (converted from units of GHz^2 to Hz^2)

    # nu2^-2 - nu1^-2 [Hz^-2]
    freq_diff = np.array([(sr * ran[i])**(-2) - (sr * ran[i + 1])**(-2) for i in range(ran.size - 1)])
    np.append(freq_diff, 0)
    assert freq_diff.size == ran.size

    # change in time between two frequencies (∆t) [ms]
    t = dm * kdm * freq_diff

    # convert time to number of samples
    repeats = np.array(t * samp_rate / 1000, dtype='int')
    repeats[0] = repeats[0] * -1  # because conversion from 'inf' yields large negative int
    return repeats
