"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

# imports from read_data_sample.py
import digital_rf
import datetime
import dateutil.parser
import calendar


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """
    Embedded Python Block: adaptation of read_data_sample.py that
    reads raw data samples (.h5) with Digital RF and then outputs five
    vectors of data points (complex64).
    """

    def __init__(self, parent_path='/Volumes/NO NAME/pulsar/2022-05-26/rf_data/', channel='misa-l2', target='1971-01-01T00:00:00', veclen=1024):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Digital RF Data Vector Source',   # will show up in GRC
            in_sig=None,
            out_sig=[(np.complex64, veclen)]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.parent_path = parent_path
        self.channel = channel
        self.target = target
        self.veclen = veclen

        # getting channel stuff (reader, bounds, properties, dates)
        self.do = digital_rf.DigitalRFReader(parent_path)
        self.s, self.e = self.do.get_bounds(self.channel)
        self.properties = self.do.get_properties(self.channel)
        self.sr = self.properties['sample_rate_numerator'] / self.properties['sample_rate_denominator']
        self.sd = datetime.datetime.utcfromtimestamp(self.s / self.sr)
        self.ed = datetime.datetime.utcfromtimestamp(self.e / self.sr)

        # initialize number of samples, start index, number of vectors
        self.sindex = self.s
        self.timesthru = 0

        #self.dvec = self.do.read_vector_c81d(self.s, self.veclen, self.channel)

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        dvec = self.do.read_vector_c81d(self.sindex, self.veclen, self.channel)
        self.timesthru += 1
        self.sindex = (self.timesthru * self.veclen) + self.s
        if len(dvec) < self.veclen:
            np.append(dvec, np.zeros(self.veclen - len(dvec)))
        output_items[0][:] = dvec
        return len(output_items[0])
