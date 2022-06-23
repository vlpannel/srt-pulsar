#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Channelize DRF Data
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

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.filter import pfb
import gr_digital_rf
import numpy as np; import gr_digital_rf
import store_channels_chan_name as chan_name  # embedded python module



from gnuradio import qtgui

class store_channels(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Channelize DRF Data", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Channelize DRF Data")
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

        self.settings = Qt.QSettings("GNU Radio", "store_channels")

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
        self.subchannels = subchannels = 2
        self.samp_rate = samp_rate = 1e6

        ##################################################
        # Blocks
        ##################################################
        self.pfb_channelizer_ccf_0 = pfb.channelizer_ccf(
            3,
            [],
            1.0,
            100)
        self.pfb_channelizer_ccf_0.set_channel_map([])
        self.pfb_channelizer_ccf_0.declare_sample_delay(0)
        self.gr_digital_rf_digital_rf_source_0 = gr_digital_rf.digital_rf_source(
            "/Volumes/NO Name/pulsar/2022-05-26/rf_data",
            channels=[
                'misa-l2',
            ],
            start=[
                1653595200000000,
            ],
            end=[
                1653602399999999,
            ],
            repeat=False,
            throttle=False,
            gapless=False,
            min_chunksize=None,
        )
        self.gr_digital_rf_digital_rf_sink_0 = gr_digital_rf.digital_rf_sink(
            '/Users/vivelpanel/Desktop/SRT UROP 2022/Spectrogram/drf_out',
            channels=[
                'ch0',
                'ch1',
                'ch2',
            ],
            dtype=np.int16,
            subdir_cadence_secs=3600,
            file_cadence_millisecs=1000,
            sample_rate_numerator=int(samp_rate),
            sample_rate_denominator=1,
            start=1653595200000000,
            ignore_tags=False,
            is_complex=False,
            num_subchannels=1,
            uuid_str=None,
            center_frequencies=(
                None
            ),
            metadata={},
            is_continuous=True,
            compression_level=0,
            checksum=False,
            marching_periods=True,
            stop_on_skipped=False,
            stop_on_time_tag=False,
            debug=False,
            min_chunksize=None,
        )
        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_short*1, subchannels)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_short*1, samp_rate,True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_interleaved_short_to_complex_0 = blocks.interleaved_short_to_complex(False, False,1.0)
        self.blocks_complex_to_interleaved_short_0_1 = blocks.complex_to_interleaved_short(False,1.0)
        self.blocks_complex_to_interleaved_short_0_0 = blocks.complex_to_interleaved_short(False,1.0)
        self.blocks_complex_to_interleaved_short_0 = blocks.complex_to_interleaved_short(False,1.0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_interleaved_short_0, 0), (self.gr_digital_rf_digital_rf_sink_0, 0))
        self.connect((self.blocks_complex_to_interleaved_short_0_0, 0), (self.gr_digital_rf_digital_rf_sink_0, 2))
        self.connect((self.blocks_complex_to_interleaved_short_0_1, 0), (self.gr_digital_rf_digital_rf_sink_0, 1))
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.pfb_channelizer_ccf_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_interleaved_short_to_complex_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0, 0), (self.blocks_vector_to_streams_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 0), (self.blocks_complex_to_interleaved_short_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 2), (self.blocks_complex_to_interleaved_short_0_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 1), (self.blocks_complex_to_interleaved_short_0_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "store_channels")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_subchannels(self):
        return self.subchannels

    def set_subchannels(self, subchannels):
        self.subchannels = subchannels

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)




def main(top_block_cls=store_channels, options=None):

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
