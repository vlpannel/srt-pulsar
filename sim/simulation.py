#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
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
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.filter import pfb
import mitarspysigproc.filtertools
import numpy as np
import simulation_pulspy as pulspy  # embedded python module



from gnuradio import qtgui

class simulation(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "simulation")

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
        self.period = period = np.arange(.5, 0, -.0000001).size * samp_rate
        self.per_samps = per_samps = int(np.arange(.5, 0, -.0000001).size)
        self.decimation = decimation = int(1)

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=decimation,
                taps=[],
                fractional_bw=0)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.qwidget(), Qt.QWidget)

        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
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

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win, 0, 0, 1, 9)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 9):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.pfb_channelizer_ccf_0 = pfb.channelizer_ccf(
            31,
            mitarspysigproc.filtertools.kaiser_coeffs(31),
            1.0,
            100)
        self.pfb_channelizer_ccf_0.set_channel_map([])
        self.pfb_channelizer_ccf_0.declare_sample_delay(0)
        self.channels_channel_model2_0 = channels.channel_model2(
            noise_voltage=10.0,
            epsilon=1.0,
            taps=[1.0 + 1.0j],
            noise_seed=0,
            block_tags=False)
        self.blocks_vector_source_x_0 = blocks.vector_source_f(np.arange(.5, 0, -.0000001), True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, 1024)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_float*1024, '/Users/vivelpanel/Desktop/vecfile', False)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, .25, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.channels_channel_model2_0, 2))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.channels_channel_model2_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.channels_channel_model2_0, 1))
        self.connect((self.channels_channel_model2_0, 0), (self.pfb_channelizer_ccf_0, 0))
        self.connect((self.channels_channel_model2_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 1), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 19), (self.blocks_null_sink_0, 14))
        self.connect((self.pfb_channelizer_ccf_0, 10), (self.blocks_null_sink_0, 5))
        self.connect((self.pfb_channelizer_ccf_0, 24), (self.blocks_null_sink_0, 19))
        self.connect((self.pfb_channelizer_ccf_0, 11), (self.blocks_null_sink_0, 6))
        self.connect((self.pfb_channelizer_ccf_0, 13), (self.blocks_null_sink_0, 8))
        self.connect((self.pfb_channelizer_ccf_0, 15), (self.blocks_null_sink_0, 10))
        self.connect((self.pfb_channelizer_ccf_0, 20), (self.blocks_null_sink_0, 15))
        self.connect((self.pfb_channelizer_ccf_0, 16), (self.blocks_null_sink_0, 11))
        self.connect((self.pfb_channelizer_ccf_0, 18), (self.blocks_null_sink_0, 13))
        self.connect((self.pfb_channelizer_ccf_0, 8), (self.blocks_null_sink_0, 3))
        self.connect((self.pfb_channelizer_ccf_0, 9), (self.blocks_null_sink_0, 4))
        self.connect((self.pfb_channelizer_ccf_0, 12), (self.blocks_null_sink_0, 7))
        self.connect((self.pfb_channelizer_ccf_0, 26), (self.blocks_null_sink_0, 21))
        self.connect((self.pfb_channelizer_ccf_0, 22), (self.blocks_null_sink_0, 17))
        self.connect((self.pfb_channelizer_ccf_0, 17), (self.blocks_null_sink_0, 12))
        self.connect((self.pfb_channelizer_ccf_0, 5), (self.blocks_null_sink_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 14), (self.blocks_null_sink_0, 9))
        self.connect((self.pfb_channelizer_ccf_0, 6), (self.blocks_null_sink_0, 1))
        self.connect((self.pfb_channelizer_ccf_0, 23), (self.blocks_null_sink_0, 18))
        self.connect((self.pfb_channelizer_ccf_0, 25), (self.blocks_null_sink_0, 20))
        self.connect((self.pfb_channelizer_ccf_0, 21), (self.blocks_null_sink_0, 16))
        self.connect((self.pfb_channelizer_ccf_0, 7), (self.blocks_null_sink_0, 2))
        self.connect((self.pfb_channelizer_ccf_0, 2), (self.blocks_null_sink_1, 1))
        self.connect((self.pfb_channelizer_ccf_0, 27), (self.blocks_null_sink_1, 4))
        self.connect((self.pfb_channelizer_ccf_0, 30), (self.blocks_null_sink_1, 7))
        self.connect((self.pfb_channelizer_ccf_0, 1), (self.blocks_null_sink_1, 0))
        self.connect((self.pfb_channelizer_ccf_0, 29), (self.blocks_null_sink_1, 6))
        self.connect((self.pfb_channelizer_ccf_0, 3), (self.blocks_null_sink_1, 2))
        self.connect((self.pfb_channelizer_ccf_0, 4), (self.blocks_null_sink_1, 3))
        self.connect((self.pfb_channelizer_ccf_0, 28), (self.blocks_null_sink_1, 5))
        self.connect((self.pfb_channelizer_ccf_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_stream_to_vector_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_period(np.arange(.5, 0, -.0000001).size * self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_period(self):
        return self.period

    def set_period(self, period):
        self.period = period

    def get_per_samps(self):
        return self.per_samps

    def set_per_samps(self, per_samps):
        self.per_samps = per_samps

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation




def main(top_block_cls=simulation, options=None):

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
