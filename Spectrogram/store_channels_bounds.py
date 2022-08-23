# this module will be imported in the into your flowgraph

import digital_rf

source_filepath = '/Volumes/NO NAME/pulsar/2022-05-26/rf_data'
sink_filepath = '/Users/vivelpanel/Desktop/SRT UROP 2022/Spectrogram/drf_out'
d = digital_rf.DigitalRFReader(source_filepath)
channel = 'misa-l2'

def check_channel():
    """
    Checks to make sure channel is within source of RF data. Raises AssertionError if not.
    """
    try:
        assert channel in d.get_channels()
    except AssertionError:
        print('That channel isn\'t in this data!')

def sindex(offset):
    """
    Generates a start index of DRF reading by returning the index of the first sample in channel plus some offset.

    Parameters:
        offset : int
            Integer offset for how many samples after first sample should start reading.
    """
    check_channel()
    return d.get_bounds(channel)[0]

def eindex(factor):
    """
    Generates an end index of DRF reading by returning the index of a sample that is 1/factor the way through the entire series of samples.

    Parameters:
        factor : int or float
            Denominator for proportion of samples to be read, eg., if factor is 10 then 1/10 of samples will be read.
    """
    check_channel()
    s, e = d.get_bounds(channel)
    return (e - s) / factor
