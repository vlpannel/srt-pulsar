#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Tuner
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
from gnuradio.filter import firdes
import sip
from gnuradio import audio
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation



from gnuradio import qtgui

class tuner_top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Tuner", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Tuner")
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

        self.settings = Qt.QSettings("GNU Radio", "tuner_top_block")

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
        self.width = width = 10
        self.samp_rate = samp_rate = 32000
        self.low_e = low_e = 82.41
        self.high_e = high_e = 329.63
        self.g = g = 196.0
        self.d = d = 146.83
        self.b = b = 246.94
        self.a = a = 110.0

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_sink_x_0_3_0 = qtgui.sink_f(
            4096, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            high_e, #fc
            samp_rate, #bw
            "", #name
            False, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_3_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_3_0_win = sip.wrapinstance(self.qtgui_sink_x_0_3_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_3_0.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_3_0_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_sink_x_0_3 = qtgui.sink_f(
            4096, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            b, #fc
            samp_rate, #bw
            "", #name
            False, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_3.set_update_time(1.0/10)
        self._qtgui_sink_x_0_3_win = sip.wrapinstance(self.qtgui_sink_x_0_3.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_3.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_3_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_sink_x_0_2 = qtgui.sink_f(
            4096, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            g, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_2.set_update_time(1.0/10)
        self._qtgui_sink_x_0_2_win = sip.wrapinstance(self.qtgui_sink_x_0_2.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_2.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_2_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_sink_x_0_1 = qtgui.sink_f(
            4096, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            d, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0_1.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_win = sip.wrapinstance(self.qtgui_sink_x_0_1.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_1.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_1_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_sink_x_0_0 = qtgui.sink_f(
            4096, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            a, #fc
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

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_sink_x_0 = qtgui.sink_f(
            4096, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            low_e, #fc
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

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.band_pass_filter_0_3_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                high_e - width,
                high_e + width,
                width / 2,
                window.WIN_BLACKMAN,
                6.76))
        self.band_pass_filter_0_3 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                b - width,
                b + width,
                width / 2,
                window.WIN_BLACKMAN,
                6.76))
        self.band_pass_filter_0_2 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                g - width,
                g + width,
                width / 2,
                window.WIN_BLACKMAN,
                6.76))
        self.band_pass_filter_0_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                d - width,
                d + width,
                width / 2,
                window.WIN_BLACKMAN,
                6.76))
        self.band_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                a - width,
                a + width,
                width / 2,
                window.WIN_BLACKMAN,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                low_e - width,
                low_e + width,
                width / 2,
                window.WIN_BLACKMAN,
                6.76))
        self.audio_source_0 = audio.source(samp_rate, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.audio_source_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.audio_source_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.audio_source_0, 0), (self.band_pass_filter_0_1, 0))
        self.connect((self.audio_source_0, 0), (self.band_pass_filter_0_2, 0))
        self.connect((self.audio_source_0, 0), (self.band_pass_filter_0_3, 0))
        self.connect((self.audio_source_0, 0), (self.band_pass_filter_0_3_1, 0))
        self.connect((self.band_pass_filter_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.qtgui_sink_x_0_0, 0))
        self.connect((self.band_pass_filter_0_1, 0), (self.qtgui_sink_x_0_1, 0))
        self.connect((self.band_pass_filter_0_2, 0), (self.qtgui_sink_x_0_2, 0))
        self.connect((self.band_pass_filter_0_3, 0), (self.qtgui_sink_x_0_3, 0))
        self.connect((self.band_pass_filter_0_3_1, 0), (self.qtgui_sink_x_0_3_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "tuner_top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.low_e - self.width, self.low_e + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.a - self.width, self.a + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(1, self.samp_rate, self.d - self.width, self.d + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.band_pass_filter_0_2.set_taps(firdes.band_pass(1, self.samp_rate, self.g - self.width, self.g + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.band_pass_filter_0_3.set_taps(firdes.band_pass(1, self.samp_rate, self.b - self.width, self.b + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.band_pass_filter_0_3_1.set_taps(firdes.band_pass(1, self.samp_rate, self.high_e - self.width, self.high_e + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.low_e - self.width, self.low_e + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.a - self.width, self.a + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(1, self.samp_rate, self.d - self.width, self.d + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.band_pass_filter_0_2.set_taps(firdes.band_pass(1, self.samp_rate, self.g - self.width, self.g + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.band_pass_filter_0_3.set_taps(firdes.band_pass(1, self.samp_rate, self.b - self.width, self.b + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.band_pass_filter_0_3_1.set_taps(firdes.band_pass(1, self.samp_rate, self.high_e - self.width, self.high_e + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.qtgui_sink_x_0.set_frequency_range(self.low_e, self.samp_rate)
        self.qtgui_sink_x_0_0.set_frequency_range(self.a, self.samp_rate)
        self.qtgui_sink_x_0_1.set_frequency_range(self.d, self.samp_rate)
        self.qtgui_sink_x_0_2.set_frequency_range(self.g, self.samp_rate)
        self.qtgui_sink_x_0_3.set_frequency_range(self.b, self.samp_rate)
        self.qtgui_sink_x_0_3_0.set_frequency_range(self.high_e, self.samp_rate)

    def get_low_e(self):
        return self.low_e

    def set_low_e(self, low_e):
        self.low_e = low_e
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.low_e - self.width, self.low_e + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.qtgui_sink_x_0.set_frequency_range(self.low_e, self.samp_rate)

    def get_high_e(self):
        return self.high_e

    def set_high_e(self, high_e):
        self.high_e = high_e
        self.band_pass_filter_0_3_1.set_taps(firdes.band_pass(1, self.samp_rate, self.high_e - self.width, self.high_e + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.qtgui_sink_x_0_3_0.set_frequency_range(self.high_e, self.samp_rate)

    def get_g(self):
        return self.g

    def set_g(self, g):
        self.g = g
        self.band_pass_filter_0_2.set_taps(firdes.band_pass(1, self.samp_rate, self.g - self.width, self.g + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.qtgui_sink_x_0_2.set_frequency_range(self.g, self.samp_rate)

    def get_d(self):
        return self.d

    def set_d(self, d):
        self.d = d
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(1, self.samp_rate, self.d - self.width, self.d + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.qtgui_sink_x_0_1.set_frequency_range(self.d, self.samp_rate)

    def get_b(self):
        return self.b

    def set_b(self, b):
        self.b = b
        self.band_pass_filter_0_3.set_taps(firdes.band_pass(1, self.samp_rate, self.b - self.width, self.b + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.qtgui_sink_x_0_3.set_frequency_range(self.b, self.samp_rate)

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, self.a - self.width, self.a + self.width, self.width / 2, window.WIN_BLACKMAN, 6.76))
        self.qtgui_sink_x_0_0.set_frequency_range(self.a, self.samp_rate)




def main(top_block_cls=tuner_top_block, options=None):

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
