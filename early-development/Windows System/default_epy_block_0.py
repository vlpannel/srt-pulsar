"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

from __future__ import absolute_import, division, print_function

import os
import traceback

import gnuradio.blocks
import h5py
import pmt
import six


import numpy as np
from gnuradio import gr
import digital_rf as drf
from digital_rf import DigitalRFReader, util


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Modified version of DRF Source"""

    def __init__(self, data_dir=r'E:\pulsar\2022-05-26\usrp-rx0-r_20220526T200000_20220526T210800\rf_data', chan='misa-l2', repeat=False):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Modified DRF Source',
            in_sig=[],
            out_sig=[np.complex64]
        )
        self.data_dir = data_dir
        self.chan = chan
        self.repeat = repeat    # repeat flag: currently nonfunctional, but may be useful later
        
        self.do = drf.DigitalRFReader(self.data_dir)
        self.bounds = self.do.get_bounds(self.chan)
        self.prop = self.do.get_properties(self.chan)
        
        self.index = self.bounds[0]# + (16 * 1000000)     # start at first sample
        self.result = 0
        
    def work(self, input_items, output_items):
        out = output_items[0]
        nsamples = len(out)
        data = self.do.read_vector(self.index, nsamples, self.chan)
        self.index += nsamples
        
        output_items[0][:] = data
        
        return len(output_items[0])
    '''
    def work(self, input_items, output_items):
        #ADDED CONTENT
        self._start_sample = util.parse_identifier_to_sample(
            None, self.prop["samples_per_second"], self.bounds[0]
        )
        self._end_sample = util.parse_identifier_to_sample(
            None, self.prop["samples_per_second"], self.bounds[0]
        )
        self._gapless = True
        if self._start_sample is None:
            self._read_start_sample = self.bounds[0]
        else:
            self._read_start_sample = self._start_sample
        
        out = output_items[0]
        nsamples = len(out)
        next_index = 0
        # repeat reading until we succeed or return
        while next_index < nsamples:
            read_start = self._read_start_sample
            # read_end is inclusive, hence the -1
            read_end = self._read_start_sample + (nsamples - next_index) - 1
            # creating a read function that has an output argument so data can
            # be copied directly would be nice
            # also should move EOFError checking into reader once watchdog
            # bounds functionality is implemented
            try:
                if self._end_sample is None:
                    if read_end > self.bounds[1]:
                        self.bounds = self._Reader.get_bounds(self.chan)
                        read_end = min(read_end, self.bounds[1])
                else:
                    if read_end > self._end_sample:
                        read_end = self._end_sample
                if read_start > read_end:
                    raise EOFError
                # read data
                data_dict = self.do.read(read_start, read_end, self.chan)
                # handled all samples through read_end regardless of whether
                # they were written to the output vector
                self._read_start_sample = read_end + 1
                # early escape for no data
                if not data_dict:
                    if self._gapless:
                        # output empty samples if no data and gapless output
                        stop_index = next_index + read_end + 1 - read_start
                        out[next_index:stop_index] = self._fillvalue
                        next_index = stop_index
                    else:
                        # clear any existing tags
                        self._tag_queue.clear()
                        # add tag at next potential sample to indicate skip
                        self._queue_tags(self._read_start_sample, {})
                    continue
                # read corresponding metadata
                if self._DMDReader is not None:
                    meta_dict = self._DMDReader.read(read_start, read_end)
                    for sample, meta in meta_dict.items():
                        # add tags from Digital Metadata
                        # (in addition to default time and rate tags)
                        # eliminate sample_rate_* tags with duplicate info
                        meta.pop("sample_rate_denominator", None)
                        meta.pop("sample_rate_numerator", None)
                        # get center frequencies for rx_freq tag, squeeze()[()]
                        # to get single value if possible else pass as an array
                        cf = meta.pop("center_frequencies", None)
                        if cf is not None:
                            cf = cf.ravel().squeeze()[()]
                        tags = dict(
                            rx_freq=cf,
                            # all other metadata goes in metadata tag
                            metadata=meta,
                        )
                        self._queue_tags(sample, tags)
                # add data and tags to output
                next_continuous_sample = read_start
                for sample, data in data_dict.items():
                    # detect data skip
                    if sample > next_continuous_sample:
                        if self._gapless:
                            # advance output by skipped number of samples
                            nskipped = sample - next_continuous_sample
                            sample_index = next_index + nskipped
                            out[next_index:sample_index] = self._fillvalue
                            next_index = sample_index
                        else:
                            # emit new time tag at sample to indicate skip
                            self._queue_tags(sample, {})
                    # output data
                    n = data.shape[0]
                    stop_index = next_index + n
                    end_sample = sample + n
                    out_dest = out[next_index:stop_index]
                    data_arr = data.squeeze()
                    out_dest[:] = data_arr
                    # overwrite missing values with fill values
                    missing_val_idx = self._ismissing(data_arr)
                    out_dest[missing_val_idx] = self._fillvalue
                    # output tags
                    for tag_sample in sorted(self._tag_queue.keys()):
                        if tag_sample < sample:
                            # drop tags from before current data block
                            del self._tag_queue[tag_sample]
                            continue
                        elif tag_sample >= end_sample:
                            # wait to output tags from after current data block
                            break
                        offset = (
                            self.nitems_written(0)  # offset @ start of work
                            + next_index  # additional offset of data block
                            + (tag_sample - sample)
                        )
                        tag_dict = self._tag_queue.pop(tag_sample)
                        for name, val in tag_dict.items():
                            self.add_item_tag(
                                0, offset, pmt.intern(name), val, self._id
                            )
                    # advance next output index and continuous sample
                    next_index = stop_index  # <=== next_index += n
                    next_continuous_sample = end_sample
            except EOFError:
                if self._repeat:
                    if self._start_sample is None:
                        self._read_start_sample = self.bounds[0]
                    else:
                        self._read_start_sample = self._start_sample
                    self._queue_tags(self._read_start_sample, {})
                    continue
                else:
                    break
        if next_index == 0:
            # return WORK_DONE
            return -1
        return next_index
        '''
