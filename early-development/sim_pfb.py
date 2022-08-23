#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: vlpannel
# GNU Radio version: 3.10.3.0

from packaging.version import Version as StrictVersion

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
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.filter import pfb
from mitarspysigproc import filtertools
import digital_rf
import numpy as np; import gr_digital_rf
import sim_pfb_epy_block_0 as epy_block_0  # embedded python block



from gnuradio import qtgui

class sim_pfb(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
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

        self.settings = Qt.QSettings("GNU Radio", "sim_pfb")

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
        self.samp_rate = samp_rate = 1e6

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_sink_x_0_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self.pfb_channelizer_ccf_0 = pfb.channelizer_ccf(
            31,
            filtertools.kaiser_coeffs(31),
            1.0,
            100)
        self.pfb_channelizer_ccf_0.set_channel_map([])
        self.pfb_channelizer_ccf_0.declare_sample_delay(0)
        self.gr_digital_rf_digital_rf_sink_0 = gr_digital_rf.digital_rf_sink(
            'C:\\\\Users\\\\vlpannel\\\\Desktop\\\\pfbdata',
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
            dtype=np.complex64,
            subdir_cadence_secs=3600,
            file_cadence_millisecs=1000,
            sample_rate_numerator=int(samp_rate),
            sample_rate_denominator=1,
            start=None,
            ignore_tags=False,
            is_complex=True,
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
        self.epy_block_0 = epy_block_0.blk(datadir="C:\\Users\\vlpannel\\Desktop\\raw", chan="ch0")
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 200)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.pfb_channelizer_ccf_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 15), (self.blocks_null_sink_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 16), (self.blocks_null_sink_0, 1))
        self.connect((self.pfb_channelizer_ccf_0, 24), (self.gr_digital_rf_digital_rf_sink_0, 22))
        self.connect((self.pfb_channelizer_ccf_0, 3), (self.gr_digital_rf_digital_rf_sink_0, 3))
        self.connect((self.pfb_channelizer_ccf_0, 28), (self.gr_digital_rf_digital_rf_sink_0, 26))
        self.connect((self.pfb_channelizer_ccf_0, 30), (self.gr_digital_rf_digital_rf_sink_0, 28))
        self.connect((self.pfb_channelizer_ccf_0, 23), (self.gr_digital_rf_digital_rf_sink_0, 21))
        self.connect((self.pfb_channelizer_ccf_0, 22), (self.gr_digital_rf_digital_rf_sink_0, 20))
        self.connect((self.pfb_channelizer_ccf_0, 1), (self.gr_digital_rf_digital_rf_sink_0, 1))
        self.connect((self.pfb_channelizer_ccf_0, 11), (self.gr_digital_rf_digital_rf_sink_0, 11))
        self.connect((self.pfb_channelizer_ccf_0, 27), (self.gr_digital_rf_digital_rf_sink_0, 25))
        self.connect((self.pfb_channelizer_ccf_0, 18), (self.gr_digital_rf_digital_rf_sink_0, 16))
        self.connect((self.pfb_channelizer_ccf_0, 6), (self.gr_digital_rf_digital_rf_sink_0, 6))
        self.connect((self.pfb_channelizer_ccf_0, 4), (self.gr_digital_rf_digital_rf_sink_0, 4))
        self.connect((self.pfb_channelizer_ccf_0, 13), (self.gr_digital_rf_digital_rf_sink_0, 13))
        self.connect((self.pfb_channelizer_ccf_0, 17), (self.gr_digital_rf_digital_rf_sink_0, 15))
        self.connect((self.pfb_channelizer_ccf_0, 14), (self.gr_digital_rf_digital_rf_sink_0, 14))
        self.connect((self.pfb_channelizer_ccf_0, 2), (self.gr_digital_rf_digital_rf_sink_0, 2))
        self.connect((self.pfb_channelizer_ccf_0, 9), (self.gr_digital_rf_digital_rf_sink_0, 9))
        self.connect((self.pfb_channelizer_ccf_0, 25), (self.gr_digital_rf_digital_rf_sink_0, 23))
        self.connect((self.pfb_channelizer_ccf_0, 0), (self.gr_digital_rf_digital_rf_sink_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 26), (self.gr_digital_rf_digital_rf_sink_0, 24))
        self.connect((self.pfb_channelizer_ccf_0, 7), (self.gr_digital_rf_digital_rf_sink_0, 7))
        self.connect((self.pfb_channelizer_ccf_0, 10), (self.gr_digital_rf_digital_rf_sink_0, 10))
        self.connect((self.pfb_channelizer_ccf_0, 8), (self.gr_digital_rf_digital_rf_sink_0, 8))
        self.connect((self.pfb_channelizer_ccf_0, 21), (self.gr_digital_rf_digital_rf_sink_0, 19))
        self.connect((self.pfb_channelizer_ccf_0, 29), (self.gr_digital_rf_digital_rf_sink_0, 27))
        self.connect((self.pfb_channelizer_ccf_0, 19), (self.gr_digital_rf_digital_rf_sink_0, 17))
        self.connect((self.pfb_channelizer_ccf_0, 20), (self.gr_digital_rf_digital_rf_sink_0, 18))
        self.connect((self.pfb_channelizer_ccf_0, 5), (self.gr_digital_rf_digital_rf_sink_0, 5))
        self.connect((self.pfb_channelizer_ccf_0, 12), (self.gr_digital_rf_digital_rf_sink_0, 12))
        self.connect((self.pfb_channelizer_ccf_0, 10), (self.qtgui_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "sim_pfb")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate)




def main(top_block_cls=sim_pfb, options=None):

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
