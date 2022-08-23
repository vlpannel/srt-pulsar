#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Prototype Flowgraph: Folding
# Author: vivelpanel
# GNU Radio version: 3.9.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import gr_digital_rf
import prototype_folding_epy_block_0 as epy_block_0  # embedded python block
import prototype_folding_epy_block_0_0 as epy_block_0_0  # embedded python block
import prototype_folding_epy_block_0_0_0 as epy_block_0_0_0  # embedded python block
import prototype_folding_epy_block_0_0_0_0 as epy_block_0_0_0_0  # embedded python block
import prototype_folding_epy_block_0_0_1 as epy_block_0_0_1  # embedded python block
import prototype_folding_epy_block_0_1 as epy_block_0_1  # embedded python block
import prototype_folding_epy_block_0_1_0 as epy_block_0_1_0  # embedded python block



from gnuradio import qtgui

class prototype_folding(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Prototype Flowgraph: Folding", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Prototype Flowgraph: Folding")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "prototype_folding")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.sr = sr = 1000000
        self.secs = secs = 120
        self.samp_rate = samp_rate = 32000
        self.pfb_data = pfb_data = "/Users/vivelpanel/pfbdata"
        self.period = period = 33.5028583*1e-3
        self.num_subchannels = num_subchannels = 1
        self.nsamps = nsamps = int(secs*sr)
        self.channel = channel = 'ch0'
        self.bins = bins = 1024

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            1024,
            0,
            1.0,
            "Phase",
            "Power",
            "",
            7, # Number of inputs
            None # parent
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(7):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_win)
        self.gr_digital_rf_digital_rf_source_0_0 = gr_digital_rf.digital_rf_source(
            pfb_data,
            channels=[
                'ch0',
                'ch1',
                'ch2',
                'ch3',
                'ch4',
                'ch5',
                'ch6',
                'ch7',
                'ch8',
                'ch9',
                'ch10',
                'ch11',
                'ch12',
                'ch13',
                'ch14',
                'ch15',
                'ch16',
                'ch17',
                'ch18',
                'ch19',
                'ch20',
                'ch21',
                'ch22',
                'ch23',
                'ch24',
                'ch25',
                'ch26',
                'ch27',
                'ch28',
            ],
            start=[
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            ],
            end=[
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            ],
            repeat=False,
            throttle=False,
            gapless=False,
            min_chunksize=None,
        )
        self.epy_block_0_1_0 = epy_block_0_1_0.blk(nsamps=nsamps, samp_rate=samp_rate, Nbins=bins, pfold=period)
        self.epy_block_0_1 = epy_block_0_1.blk(nsamps=nsamps, samp_rate=samp_rate, Nbins=bins, pfold=period)
        self.epy_block_0_0_1 = epy_block_0_0_1.blk(nsamps=nsamps, samp_rate=samp_rate, Nbins=bins, pfold=period)
        self.epy_block_0_0_0_0 = epy_block_0_0_0_0.blk(nsamps=nsamps, samp_rate=samp_rate, Nbins=bins, pfold=period)
        self.epy_block_0_0_0 = epy_block_0_0_0.blk(nsamps=nsamps, samp_rate=samp_rate, Nbins=bins, pfold=period)
        self.epy_block_0_0 = epy_block_0_0.blk(nsamps=nsamps, samp_rate=samp_rate, Nbins=bins, pfold=period)
        self.epy_block_0 = epy_block_0.blk(nsamps=nsamps, samp_rate=samp_rate, Nbins=bins, pfold=period)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_vector_0_4 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_3_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_3 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_2_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_2_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_2_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_2_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_2 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_1_2 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_1_1_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_1_1_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_1_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_1_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_1_0_0_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_1_0_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_1_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_1_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_1_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_0_2 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_0_1_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_0_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_0_0_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_0_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nsamps)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_2 = blocks.null_sink(gr.sizeof_gr_complex*nsamps)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_float*bins)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_msgpair_to_var_0 = blocks.msg_pair_to_var(self.set_sr)
        self.blocks_msg_meta_to_pair_0 = blocks.meta_to_pair('samples_per_second','samp_rate')


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_msg_meta_to_pair_0, 'outpair'), (self.blocks_msgpair_to_var_0, 'inpair'))
        self.msg_connect((self.gr_digital_rf_digital_rf_source_0_0, 'properties'), (self.blocks_msg_meta_to_pair_0, 'inmeta'))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.epy_block_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0_0, 0), (self.blocks_null_sink_2, 0))
        self.connect((self.blocks_stream_to_vector_0_0_0_0, 0), (self.blocks_null_sink_2, 6))
        self.connect((self.blocks_stream_to_vector_0_0_0_0_0, 0), (self.blocks_null_sink_2, 18))
        self.connect((self.blocks_stream_to_vector_0_0_0_0_0_0, 0), (self.epy_block_0_0_1, 0))
        self.connect((self.blocks_stream_to_vector_0_0_0_1, 0), (self.blocks_null_sink_2, 12))
        self.connect((self.blocks_stream_to_vector_0_0_1, 0), (self.blocks_null_sink_2, 3))
        self.connect((self.blocks_stream_to_vector_0_0_1_0, 0), (self.blocks_null_sink_2, 15))
        self.connect((self.blocks_stream_to_vector_0_0_2, 0), (self.blocks_null_sink_2, 9))
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.epy_block_0_1, 0))
        self.connect((self.blocks_stream_to_vector_0_1_0, 0), (self.blocks_null_sink_2, 1))
        self.connect((self.blocks_stream_to_vector_0_1_0_0, 0), (self.blocks_null_sink_2, 7))
        self.connect((self.blocks_stream_to_vector_0_1_0_0_0, 0), (self.blocks_null_sink_2, 19))
        self.connect((self.blocks_stream_to_vector_0_1_0_0_0_0, 0), (self.epy_block_0_1_0, 0))
        self.connect((self.blocks_stream_to_vector_0_1_0_0_0_0_0, 0), (self.epy_block_0_0_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_1_0_1, 0), (self.blocks_null_sink_2, 13))
        self.connect((self.blocks_stream_to_vector_0_1_1, 0), (self.blocks_null_sink_2, 4))
        self.connect((self.blocks_stream_to_vector_0_1_1_0, 0), (self.blocks_null_sink_2, 16))
        self.connect((self.blocks_stream_to_vector_0_1_1_0_0, 0), (self.blocks_null_sink_2, 20))
        self.connect((self.blocks_stream_to_vector_0_1_2, 0), (self.blocks_null_sink_2, 10))
        self.connect((self.blocks_stream_to_vector_0_2, 0), (self.epy_block_0_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_2_0, 0), (self.blocks_null_sink_2, 5))
        self.connect((self.blocks_stream_to_vector_0_2_0_0, 0), (self.blocks_null_sink_2, 17))
        self.connect((self.blocks_stream_to_vector_0_2_0_0_0, 0), (self.blocks_null_sink_2, 21))
        self.connect((self.blocks_stream_to_vector_0_2_1, 0), (self.blocks_null_sink_2, 11))
        self.connect((self.blocks_stream_to_vector_0_3, 0), (self.blocks_null_sink_2, 2))
        self.connect((self.blocks_stream_to_vector_0_3_0, 0), (self.blocks_null_sink_2, 14))
        self.connect((self.blocks_stream_to_vector_0_4, 0), (self.blocks_null_sink_2, 8))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.epy_block_0, 1), (self.blocks_null_sink_1, 0))
        self.connect((self.epy_block_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.epy_block_0_0, 1), (self.blocks_null_sink_1, 1))
        self.connect((self.epy_block_0_0, 0), (self.qtgui_vector_sink_f_0, 1))
        self.connect((self.epy_block_0_0_0, 1), (self.blocks_null_sink_1, 3))
        self.connect((self.epy_block_0_0_0, 0), (self.qtgui_vector_sink_f_0, 3))
        self.connect((self.epy_block_0_0_0_0, 1), (self.blocks_null_sink_1, 6))
        self.connect((self.epy_block_0_0_0_0, 0), (self.qtgui_vector_sink_f_0, 6))
        self.connect((self.epy_block_0_0_1, 1), (self.blocks_null_sink_1, 4))
        self.connect((self.epy_block_0_0_1, 0), (self.qtgui_vector_sink_f_0, 4))
        self.connect((self.epy_block_0_1, 1), (self.blocks_null_sink_1, 2))
        self.connect((self.epy_block_0_1, 0), (self.qtgui_vector_sink_f_0, 2))
        self.connect((self.epy_block_0_1_0, 1), (self.blocks_null_sink_1, 5))
        self.connect((self.epy_block_0_1_0, 0), (self.qtgui_vector_sink_f_0, 5))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 1), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 4), (self.blocks_stream_to_vector_0_0_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 10), (self.blocks_stream_to_vector_0_0_0_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 22), (self.blocks_stream_to_vector_0_0_0_0_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 26), (self.blocks_stream_to_vector_0_0_0_0_0_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 16), (self.blocks_stream_to_vector_0_0_0_1, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 7), (self.blocks_stream_to_vector_0_0_1, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 19), (self.blocks_stream_to_vector_0_0_1_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 13), (self.blocks_stream_to_vector_0_0_2, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 2), (self.blocks_stream_to_vector_0_1, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 5), (self.blocks_stream_to_vector_0_1_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 11), (self.blocks_stream_to_vector_0_1_0_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 23), (self.blocks_stream_to_vector_0_1_0_0_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 27), (self.blocks_stream_to_vector_0_1_0_0_0_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 28), (self.blocks_stream_to_vector_0_1_0_0_0_0_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 17), (self.blocks_stream_to_vector_0_1_0_1, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 8), (self.blocks_stream_to_vector_0_1_1, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 20), (self.blocks_stream_to_vector_0_1_1_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 24), (self.blocks_stream_to_vector_0_1_1_0_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 14), (self.blocks_stream_to_vector_0_1_2, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 3), (self.blocks_stream_to_vector_0_2, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 9), (self.blocks_stream_to_vector_0_2_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 21), (self.blocks_stream_to_vector_0_2_0_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 25), (self.blocks_stream_to_vector_0_2_0_0_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 15), (self.blocks_stream_to_vector_0_2_1, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 6), (self.blocks_stream_to_vector_0_3, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 18), (self.blocks_stream_to_vector_0_3_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0_0, 12), (self.blocks_stream_to_vector_0_4, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "prototype_folding")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sr(self):
        return self.sr

    def set_sr(self, sr):
        self.sr = sr
        self.set_nsamps(int(self.secs*self.sr))

    def get_secs(self):
        return self.secs

    def set_secs(self, secs):
        self.secs = secs
        self.set_nsamps(int(self.secs*self.sr))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.epy_block_0.samp_rate = self.samp_rate
        self.epy_block_0_0.samp_rate = self.samp_rate
        self.epy_block_0_0_0.samp_rate = self.samp_rate
        self.epy_block_0_0_0_0.samp_rate = self.samp_rate
        self.epy_block_0_0_1.samp_rate = self.samp_rate
        self.epy_block_0_1.samp_rate = self.samp_rate
        self.epy_block_0_1_0.samp_rate = self.samp_rate

    def get_pfb_data(self):
        return self.pfb_data

    def set_pfb_data(self, pfb_data):
        self.pfb_data = pfb_data

    def get_period(self):
        return self.period

    def set_period(self, period):
        self.period = period
        self.epy_block_0.pfold = self.period
        self.epy_block_0_0.pfold = self.period
        self.epy_block_0_0_0.pfold = self.period
        self.epy_block_0_0_0_0.pfold = self.period
        self.epy_block_0_0_1.pfold = self.period
        self.epy_block_0_1.pfold = self.period
        self.epy_block_0_1_0.pfold = self.period

    def get_num_subchannels(self):
        return self.num_subchannels

    def set_num_subchannels(self, num_subchannels):
        self.num_subchannels = num_subchannels

    def get_nsamps(self):
        return self.nsamps

    def set_nsamps(self, nsamps):
        self.nsamps = nsamps
        self.epy_block_0.nsamps = self.nsamps
        self.epy_block_0_0.nsamps = self.nsamps
        self.epy_block_0_0_0.nsamps = self.nsamps
        self.epy_block_0_0_0_0.nsamps = self.nsamps
        self.epy_block_0_0_1.nsamps = self.nsamps
        self.epy_block_0_1.nsamps = self.nsamps
        self.epy_block_0_1_0.nsamps = self.nsamps

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel

    def get_bins(self):
        return self.bins

    def set_bins(self, bins):
        self.bins = bins
        self.epy_block_0.Nbins = self.bins
        self.epy_block_0_0.Nbins = self.bins
        self.epy_block_0_0_0.Nbins = self.bins
        self.epy_block_0_0_0_0.Nbins = self.bins
        self.epy_block_0_0_1.Nbins = self.bins
        self.epy_block_0_1.Nbins = self.bins
        self.epy_block_0_1_0.Nbins = self.bins




def main(top_block_cls=prototype_folding, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
