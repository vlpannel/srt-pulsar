#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: DRF Pulsar Processing (Folding)
# GNU Radio version: 3.9.5.0

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import gr, blocks
import gr_digital_rf
import pmt




class drf_pulsar_flow_graph(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "DRF Pulsar Processing (Folding)", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.tlen = tlen = 1/29.7
        self.samp_rate = samp_rate = 1000000
        self.samples = samples = int(tlen*samp_rate)
        self.integration = integration = 10e3
        self.channel_start = channel_start = 1653595200000000
        self.channel_end = channel_end = 1653602399999999

        ##################################################
        # Blocks
        ##################################################
        self.gr_digital_rf_digital_rf_source_0 = gr_digital_rf.digital_rf_source(
            '/Volumes/NO NAME/pulsar/2022-05-26/rf_data',
            channels=[
                'misa-l2',
            ],
            start=[
                channel_start,
            ],
            end=[
                channel_end,
            ],
            repeat=True,
            throttle=False,
            gapless=False,
            min_chunksize=None,
        )
        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_short*1, 2)
        self.blocks_vector_to_stream_1_0 = blocks.vector_to_stream(gr.sizeof_float*1, 714520)
        self.blocks_vector_to_stream_1 = blocks.vector_to_stream(gr.sizeof_float*1, samples)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, 714520)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, samples)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_interleaved_short_to_complex_2_0 = blocks.interleaved_short_to_complex(False, False,32767.0)
        self.blocks_interleaved_short_to_complex_2 = blocks.interleaved_short_to_complex(False, False,32767.0)
        self.blocks_integrate_xx_2_0 = blocks.integrate_ff(1000, 1)
        self.blocks_integrate_xx_2 = blocks.integrate_ff(1000, 1)
        self.blocks_integrate_xx_1_0 = blocks.integrate_ff(83, 714520)
        self.blocks_integrate_xx_1 = blocks.integrate_ff(83, samples)
        self.blocks_integrate_xx_0_0 = blocks.integrate_ff(10, 1)
        self.blocks_integrate_xx_0 = blocks.integrate_ff(10, 1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, '/Users/vivelpanel/Desktop/SRT Flowgraphs/Testing Output Files/drf_output_1', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_file_meta_sink_0_0 = blocks.file_meta_sink(gr.sizeof_float*1, '/Users/vivelpanel/Desktop/SRT Flowgraphs/Testing Output Files/drf_output_sub2', samp_rate, 1, blocks.GR_FILE_FLOAT, False, 1000000, pmt.dict_add(pmt.make_dict(), pmt.intern('Initial'), pmt.from_long(3)), False)
        self.blocks_file_meta_sink_0_0.set_unbuffered(False)
        self.blocks_file_meta_sink_0 = blocks.file_meta_sink(gr.sizeof_float*1, '/Users/vivelpanel/Desktop/SRT Flowgraphs/Testing Output Files/drf_output_sub1', samp_rate, 1, blocks.GR_FILE_FLOAT, False, 1000000, pmt.dict_add(pmt.make_dict(), pmt.intern('Initial'), pmt.from_long(3)), False)
        self.blocks_file_meta_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_integrate_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_integrate_xx_0_0, 0))
        self.connect((self.blocks_integrate_xx_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_integrate_xx_0_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_integrate_xx_1, 0), (self.blocks_vector_to_stream_1, 0))
        self.connect((self.blocks_integrate_xx_1_0, 0), (self.blocks_vector_to_stream_1_0, 0))
        self.connect((self.blocks_integrate_xx_2, 0), (self.blocks_file_meta_sink_0, 0))
        self.connect((self.blocks_integrate_xx_2, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_integrate_xx_2_0, 0), (self.blocks_file_meta_sink_0_0, 0))
        self.connect((self.blocks_interleaved_short_to_complex_2, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_interleaved_short_to_complex_2_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_integrate_xx_1, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.blocks_integrate_xx_1_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))
        self.connect((self.blocks_vector_to_stream_1, 0), (self.blocks_integrate_xx_2, 0))
        self.connect((self.blocks_vector_to_stream_1_0, 0), (self.blocks_integrate_xx_2_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 0), (self.blocks_interleaved_short_to_complex_2, 0))
        self.connect((self.blocks_vector_to_streams_0, 1), (self.blocks_interleaved_short_to_complex_2_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0, 0), (self.blocks_vector_to_streams_0, 0))


    def get_tlen(self):
        return self.tlen

    def set_tlen(self, tlen):
        self.tlen = tlen
        self.set_samples(int(self.tlen*self.samp_rate))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samples(int(self.tlen*self.samp_rate))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)

    def get_samples(self):
        return self.samples

    def set_samples(self, samples):
        self.samples = samples

    def get_integration(self):
        return self.integration

    def set_integration(self, integration):
        self.integration = integration

    def get_channel_start(self):
        return self.channel_start

    def set_channel_start(self, channel_start):
        self.channel_start = channel_start

    def get_channel_end(self):
        return self.channel_end

    def set_channel_end(self, channel_end):
        self.channel_end = channel_end




def main(top_block_cls=drf_pulsar_flow_graph, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    tb.wait()


if __name__ == '__main__':
    main()
