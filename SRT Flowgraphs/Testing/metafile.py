#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Make File Meta Source
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
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
import pmt
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import gr, blocks
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import osmosdr
import time



from gnuradio import qtgui

class metafile(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Make File Meta Source", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Make File Meta Source")
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

        self.settings = Qt.QSettings("GNU Radio", "metafile")

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
        self.strobe_value = strobe_value = '0'
        self.samp_rate = samp_rate = 2.4e6
        self.freq = freq = 100e6

        ##################################################
        # Blocks
        ##################################################
        # Create the options list
        self._strobe_value_options = ['0', '1']
        # Create the labels list
        self._strobe_value_labels = ['Strobe = 0', 'Strobe = 1']
        # Create the combo box
        self._strobe_value_tool_bar = Qt.QToolBar(self)
        self._strobe_value_tool_bar.addWidget(Qt.QLabel("Tags strobe value" + ": "))
        self._strobe_value_combo_box = Qt.QComboBox()
        self._strobe_value_tool_bar.addWidget(self._strobe_value_combo_box)
        for _label in self._strobe_value_labels: self._strobe_value_combo_box.addItem(_label)
        self._strobe_value_callback = lambda i: Qt.QMetaObject.invokeMethod(self._strobe_value_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._strobe_value_options.index(i)))
        self._strobe_value_callback(self.strobe_value)
        self._strobe_value_combo_box.currentIndexChanged.connect(
            lambda i: self.set_strobe_value(self._strobe_value_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._strobe_value_tool_bar)
        self._freq_range = Range(0, 500e6, 1, 100e6, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, "'freq'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._freq_win)
        self.rtlsdr_source_1 = osmosdr.source(
            args="numchan=" + str(1) + " " + ""
        )
        self.rtlsdr_source_1.set_time_unknown_pps(osmosdr.time_spec_t())
        self.rtlsdr_source_1.set_sample_rate(samp_rate)
        self.rtlsdr_source_1.set_center_freq(freq, 0)
        self.rtlsdr_source_1.set_freq_corr(0, 0)
        self.rtlsdr_source_1.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_1.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_1.set_gain_mode(False, 0)
        self.rtlsdr_source_1.set_gain(10, 0)
        self.rtlsdr_source_1.set_if_gain(20, 0)
        self.rtlsdr_source_1.set_bb_gain(20, 0)
        self.rtlsdr_source_1.set_antenna('', 0)
        self.rtlsdr_source_1.set_bandwidth(0, 0)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            freq, #fc
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
        self.blocks_tags_strobe_1_0 = blocks.tags_strobe(gr.sizeof_gr_complex*1, pmt.intern(strobe_value), 320, pmt.intern('strobe'))
        self.blocks_tag_share_1_0 = blocks.tag_share(gr.sizeof_gr_complex, gr.sizeof_gr_complex, 1)
        self.blocks_file_meta_sink_1_0 = blocks.file_meta_sink(gr.sizeof_gr_complex*1, '/Users/vivelpanel/Desktop/SRT Flowgraphs/testmeta.bin', samp_rate, 1, blocks.GR_FILE_FLOAT, True, 1000000, pmt.dict_add(pmt.make_dict(), pmt.intern('Initial'), pmt.from_long(3)), False)
        self.blocks_file_meta_sink_1_0.set_unbuffered(False)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_tag_share_1_0, 0), (self.blocks_file_meta_sink_1_0, 0))
        self.connect((self.blocks_tags_strobe_1_0, 0), (self.blocks_tag_share_1_0, 1))
        self.connect((self.rtlsdr_source_1, 0), (self.blocks_tag_share_1_0, 0))
        self.connect((self.rtlsdr_source_1, 0), (self.qtgui_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "metafile")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_strobe_value(self):
        return self.strobe_value

    def set_strobe_value(self, strobe_value):
        self.strobe_value = strobe_value
        self._strobe_value_callback(self.strobe_value)
        self.blocks_tags_strobe_1_0.set_value(pmt.intern(self.strobe_value))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(self.freq, self.samp_rate)
        self.rtlsdr_source_1.set_sample_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.qtgui_sink_x_0.set_frequency_range(self.freq, self.samp_rate)
        self.rtlsdr_source_1.set_center_freq(self.freq, 0)




def main(top_block_cls=metafile, options=None):

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
