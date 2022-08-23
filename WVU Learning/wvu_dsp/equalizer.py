#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Equalizer
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

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class equalizer(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Equalizer", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Equalizer")
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

        self.settings = Qt.QSettings("GNU Radio", "equalizer")

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
        self.treble = treble = 1
        self.samp_rate = samp_rate = 32000
        self.mid = mid = 1
        self.bass = bass = 1

        ##################################################
        # Blocks
        ##################################################
        self._treble_range = Range(0, 10, .01, 1, 200)
        self._treble_win = RangeWidget(self._treble_range, self.set_treble, "Treble", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._treble_win)
        self._mid_range = Range(0, 10, .01, 1, 200)
        self._mid_win = RangeWidget(self._mid_range, self.set_mid, "Mid", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._mid_win)
        self._bass_range = Range(0, 10, .01, 1, 200)
        self._bass_win = RangeWidget(self._bass_range, self.set_bass, "Bass", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._bass_win)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=2,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=48000,
                decimation=32000,
                taps=[],
                fractional_bw=0)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_ff(mid)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(bass)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(treble)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate*2,
                250,
                4000,
                10,
                window.WIN_BLACKMAN,
                6.76))
        self.band_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate*2,
                4000,
                20000,
                10,
                window.WIN_BLACKMAN,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate*2,
                20,
                250,
                10,
                window.WIN_BLACKMAN,
                6.76))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_sig_source_x_2 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 10e3, 1, 0, 0)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 200, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_add_xx_0_0, 2))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.band_pass_filter_0_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_throttle_1, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.band_pass_filter_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_throttle_1, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_complex_to_float_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "equalizer")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_treble(self):
        return self.treble

    def set_treble(self, treble):
        self.treble = treble
        self.blocks_multiply_const_vxx_0.set_k(self.treble)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate*2, 20, 250, 10, window.WIN_BLACKMAN, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate*2, 4000, 20000, 10, window.WIN_BLACKMAN, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(1, self.samp_rate*2, 250, 4000, 10, window.WIN_BLACKMAN, 6.76))
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)

    def get_mid(self):
        return self.mid

    def set_mid(self, mid):
        self.mid = mid
        self.blocks_multiply_const_vxx_0_1.set_k(self.mid)

    def get_bass(self):
        return self.bass

    def set_bass(self, bass):
        self.bass = bass
        self.blocks_multiply_const_vxx_0_0.set_k(self.bass)




def main(top_block_cls=equalizer, options=None):

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
