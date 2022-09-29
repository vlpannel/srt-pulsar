#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Variable Number of Ports (32 Max)
# Author: Viveca Pannell
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



from gnuradio import qtgui

class variable_numports_handler(gr.top_block, Qt.QWidget):

    def __init__(self, criterion=lambda x: int(x in listed), listed=[]):
        gr.top_block.__init__(self, "Variable Number of Ports (32 Max)", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Variable Number of Ports (32 Max)")
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

        self.settings = Qt.QSettings("GNU Radio", "variable_numports_handler")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Parameters
        ##################################################
        self.criterion = criterion
        self.listed = listed

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.blocks_selector_0_1_9 = blocks.selector(gr.sizeof_float*1,criterion(12),0)
        self.blocks_selector_0_1_9.set_enabled(True)
        self.blocks_selector_0_1_8 = blocks.selector(gr.sizeof_float*1,criterion(11),0)
        self.blocks_selector_0_1_8.set_enabled(True)
        self.blocks_selector_0_1_7 = blocks.selector(gr.sizeof_float*1,criterion(10),0)
        self.blocks_selector_0_1_7.set_enabled(True)
        self.blocks_selector_0_1_6 = blocks.selector(gr.sizeof_float*1,criterion(9),0)
        self.blocks_selector_0_1_6.set_enabled(True)
        self.blocks_selector_0_1_5 = blocks.selector(gr.sizeof_float*1,criterion(8),0)
        self.blocks_selector_0_1_5.set_enabled(True)
        self.blocks_selector_0_1_4 = blocks.selector(gr.sizeof_float*1,criterion(7),0)
        self.blocks_selector_0_1_4.set_enabled(True)
        self.blocks_selector_0_1_3 = blocks.selector(gr.sizeof_float*1,criterion(6),0)
        self.blocks_selector_0_1_3.set_enabled(True)
        self.blocks_selector_0_1_2 = blocks.selector(gr.sizeof_float*1,criterion(5),0)
        self.blocks_selector_0_1_2.set_enabled(True)
        self.blocks_selector_0_1_15_9 = blocks.selector(gr.sizeof_float*1,criterion(28),0)
        self.blocks_selector_0_1_15_9.set_enabled(True)
        self.blocks_selector_0_1_15_8 = blocks.selector(gr.sizeof_float*1,criterion(27),0)
        self.blocks_selector_0_1_15_8.set_enabled(True)
        self.blocks_selector_0_1_15_7 = blocks.selector(gr.sizeof_float*1,criterion(26),0)
        self.blocks_selector_0_1_15_7.set_enabled(True)
        self.blocks_selector_0_1_15_6 = blocks.selector(gr.sizeof_float*1,criterion(25),0)
        self.blocks_selector_0_1_15_6.set_enabled(True)
        self.blocks_selector_0_1_15_5 = blocks.selector(gr.sizeof_float*1,criterion(24),0)
        self.blocks_selector_0_1_15_5.set_enabled(True)
        self.blocks_selector_0_1_15_4 = blocks.selector(gr.sizeof_float*1,criterion(23),0)
        self.blocks_selector_0_1_15_4.set_enabled(True)
        self.blocks_selector_0_1_15_3 = blocks.selector(gr.sizeof_float*1,criterion(22),0)
        self.blocks_selector_0_1_15_3.set_enabled(True)
        self.blocks_selector_0_1_15_2 = blocks.selector(gr.sizeof_float*1,criterion(21),0)
        self.blocks_selector_0_1_15_2.set_enabled(True)
        self.blocks_selector_0_1_15_12 = blocks.selector(gr.sizeof_float*1,criterion(31),0)
        self.blocks_selector_0_1_15_12.set_enabled(True)
        self.blocks_selector_0_1_15_11 = blocks.selector(gr.sizeof_float*1,criterion(30),0)
        self.blocks_selector_0_1_15_11.set_enabled(True)
        self.blocks_selector_0_1_15_10 = blocks.selector(gr.sizeof_float*1,criterion(29),0)
        self.blocks_selector_0_1_15_10.set_enabled(True)
        self.blocks_selector_0_1_15_1 = blocks.selector(gr.sizeof_float*1,criterion(20),0)
        self.blocks_selector_0_1_15_1.set_enabled(True)
        self.blocks_selector_0_1_15_0 = blocks.selector(gr.sizeof_float*1,criterion(19),0)
        self.blocks_selector_0_1_15_0.set_enabled(True)
        self.blocks_selector_0_1_15 = blocks.selector(gr.sizeof_float*1,criterion(18),0)
        self.blocks_selector_0_1_15.set_enabled(True)
        self.blocks_selector_0_1_14 = blocks.selector(gr.sizeof_float*1,criterion(17),0)
        self.blocks_selector_0_1_14.set_enabled(True)
        self.blocks_selector_0_1_13 = blocks.selector(gr.sizeof_float*1,criterion(16),0)
        self.blocks_selector_0_1_13.set_enabled(True)
        self.blocks_selector_0_1_12 = blocks.selector(gr.sizeof_float*1,criterion(15),0)
        self.blocks_selector_0_1_12.set_enabled(True)
        self.blocks_selector_0_1_11 = blocks.selector(gr.sizeof_float*1,criterion(14),0)
        self.blocks_selector_0_1_11.set_enabled(True)
        self.blocks_selector_0_1_10 = blocks.selector(gr.sizeof_float*1,criterion(13),0)
        self.blocks_selector_0_1_10.set_enabled(True)
        self.blocks_selector_0_1_1 = blocks.selector(gr.sizeof_float*1,criterion(4),0)
        self.blocks_selector_0_1_1.set_enabled(True)
        self.blocks_selector_0_1_0 = blocks.selector(gr.sizeof_float*1,criterion(3),0)
        self.blocks_selector_0_1_0.set_enabled(True)
        self.blocks_selector_0_1 = blocks.selector(gr.sizeof_float*1,criterion(2),0)
        self.blocks_selector_0_1.set_enabled(True)
        self.blocks_selector_0_0 = blocks.selector(gr.sizeof_float*1,criterion(1),0)
        self.blocks_selector_0_0.set_enabled(True)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_float*1,criterion(0),0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_1, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_10, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_11, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_12, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_13, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_14, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_15, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_15_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_15_1, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_15_10, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_15_11, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_15_12, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_15_2, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_15_3, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_15_4, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_15_5, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_15_6, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_15_7, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_15_8, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_15_9, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_2, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_3, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_4, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_5, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_6, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_7, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_8, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_selector_0_1_9, 0))
        self.connect((self.blocks_selector_0, 0), (self, 0))
        self.connect((self.blocks_selector_0_0, 0), (self, 1))
        self.connect((self.blocks_selector_0_1, 0), (self, 2))
        self.connect((self.blocks_selector_0_1_0, 0), (self, 13))
        self.connect((self.blocks_selector_0_1_1, 0), (self, 24))
        self.connect((self.blocks_selector_0_1_10, 0), (self, 5))
        self.connect((self.blocks_selector_0_1_11, 0), (self, 6))
        self.connect((self.blocks_selector_0_1_12, 0), (self, 7))
        self.connect((self.blocks_selector_0_1_13, 0), (self, 8))
        self.connect((self.blocks_selector_0_1_14, 0), (self, 9))
        self.connect((self.blocks_selector_0_1_15, 0), (self, 10))
        self.connect((self.blocks_selector_0_1_15_0, 0), (self, 11))
        self.connect((self.blocks_selector_0_1_15_1, 0), (self, 12))
        self.connect((self.blocks_selector_0_1_15_10, 0), (self, 22))
        self.connect((self.blocks_selector_0_1_15_11, 0), (self, 23))
        self.connect((self.blocks_selector_0_1_15_12, 0), (self, 25))
        self.connect((self.blocks_selector_0_1_15_2, 0), (self, 14))
        self.connect((self.blocks_selector_0_1_15_3, 0), (self, 15))
        self.connect((self.blocks_selector_0_1_15_4, 0), (self, 16))
        self.connect((self.blocks_selector_0_1_15_5, 0), (self, 17))
        self.connect((self.blocks_selector_0_1_15_6, 0), (self, 18))
        self.connect((self.blocks_selector_0_1_15_7, 0), (self, 19))
        self.connect((self.blocks_selector_0_1_15_8, 0), (self, 20))
        self.connect((self.blocks_selector_0_1_15_9, 0), (self, 21))
        self.connect((self.blocks_selector_0_1_2, 0), (self, 26))
        self.connect((self.blocks_selector_0_1_3, 0), (self, 27))
        self.connect((self.blocks_selector_0_1_4, 0), (self, 28))
        self.connect((self.blocks_selector_0_1_5, 0), (self, 29))
        self.connect((self.blocks_selector_0_1_6, 0), (self, 30))
        self.connect((self.blocks_selector_0_1_7, 0), (self, 31))
        self.connect((self.blocks_selector_0_1_8, 0), (self, 3))
        self.connect((self.blocks_selector_0_1_9, 0), (self, 4))
        self.connect((self, 0), (self.blocks_selector_0, 1))
        self.connect((self, 1), (self.blocks_selector_0_0, 1))
        self.connect((self, 2), (self.blocks_selector_0_1, 1))
        self.connect((self, 3), (self.blocks_selector_0_1_8, 1))
        self.connect((self, 4), (self.blocks_selector_0_1_9, 1))
        self.connect((self, 5), (self.blocks_selector_0_1_10, 1))
        self.connect((self, 6), (self.blocks_selector_0_1_11, 1))
        self.connect((self, 7), (self.blocks_selector_0_1_12, 1))
        self.connect((self, 8), (self.blocks_selector_0_1_13, 1))
        self.connect((self, 9), (self.blocks_selector_0_1_14, 1))
        self.connect((self, 10), (self.blocks_selector_0_1_15, 1))
        self.connect((self, 11), (self.blocks_selector_0_1_15_0, 1))
        self.connect((self, 12), (self.blocks_selector_0_1_15_1, 1))
        self.connect((self, 13), (self.blocks_selector_0_1_0, 1))
        self.connect((self, 14), (self.blocks_selector_0_1_15_2, 1))
        self.connect((self, 15), (self.blocks_selector_0_1_15_3, 1))
        self.connect((self, 16), (self.blocks_selector_0_1_15_4, 1))
        self.connect((self, 17), (self.blocks_selector_0_1_15_5, 1))
        self.connect((self, 18), (self.blocks_selector_0_1_15_6, 1))
        self.connect((self, 19), (self.blocks_selector_0_1_15_7, 1))
        self.connect((self, 20), (self.blocks_selector_0_1_15_8, 1))
        self.connect((self, 21), (self.blocks_selector_0_1_15_9, 1))
        self.connect((self, 22), (self.blocks_selector_0_1_15_10, 1))
        self.connect((self, 23), (self.blocks_selector_0_1_15_11, 1))
        self.connect((self, 24), (self.blocks_selector_0_1_1, 1))
        self.connect((self, 25), (self.blocks_selector_0_1_15_12, 1))
        self.connect((self, 26), (self.blocks_selector_0_1_2, 1))
        self.connect((self, 27), (self.blocks_selector_0_1_3, 1))
        self.connect((self, 28), (self.blocks_selector_0_1_4, 1))
        self.connect((self, 29), (self.blocks_selector_0_1_5, 1))
        self.connect((self, 30), (self.blocks_selector_0_1_6, 1))
        self.connect((self, 31), (self.blocks_selector_0_1_7, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "variable_numports_handler")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_criterion(self):
        return self.criterion

    def set_criterion(self, criterion):
        self.criterion = criterion
        self.blocks_selector_0.set_input_index(self.criterion(0))
        self.blocks_selector_0_0.set_input_index(self.criterion(1))
        self.blocks_selector_0_1.set_input_index(self.criterion(2))
        self.blocks_selector_0_1_0.set_input_index(self.criterion(3))
        self.blocks_selector_0_1_1.set_input_index(self.criterion(4))
        self.blocks_selector_0_1_10.set_input_index(self.criterion(13))
        self.blocks_selector_0_1_11.set_input_index(self.criterion(14))
        self.blocks_selector_0_1_12.set_input_index(self.criterion(15))
        self.blocks_selector_0_1_13.set_input_index(self.criterion(16))
        self.blocks_selector_0_1_14.set_input_index(self.criterion(17))
        self.blocks_selector_0_1_15.set_input_index(self.criterion(18))
        self.blocks_selector_0_1_15_0.set_input_index(self.criterion(19))
        self.blocks_selector_0_1_15_1.set_input_index(self.criterion(20))
        self.blocks_selector_0_1_15_10.set_input_index(self.criterion(29))
        self.blocks_selector_0_1_15_11.set_input_index(self.criterion(30))
        self.blocks_selector_0_1_15_12.set_input_index(self.criterion(31))
        self.blocks_selector_0_1_15_2.set_input_index(self.criterion(21))
        self.blocks_selector_0_1_15_3.set_input_index(self.criterion(22))
        self.blocks_selector_0_1_15_4.set_input_index(self.criterion(23))
        self.blocks_selector_0_1_15_5.set_input_index(self.criterion(24))
        self.blocks_selector_0_1_15_6.set_input_index(self.criterion(25))
        self.blocks_selector_0_1_15_7.set_input_index(self.criterion(26))
        self.blocks_selector_0_1_15_8.set_input_index(self.criterion(27))
        self.blocks_selector_0_1_15_9.set_input_index(self.criterion(28))
        self.blocks_selector_0_1_2.set_input_index(self.criterion(5))
        self.blocks_selector_0_1_3.set_input_index(self.criterion(6))
        self.blocks_selector_0_1_4.set_input_index(self.criterion(7))
        self.blocks_selector_0_1_5.set_input_index(self.criterion(8))
        self.blocks_selector_0_1_6.set_input_index(self.criterion(9))
        self.blocks_selector_0_1_7.set_input_index(self.criterion(10))
        self.blocks_selector_0_1_8.set_input_index(self.criterion(11))
        self.blocks_selector_0_1_9.set_input_index(self.criterion(12))

    def get_listed(self):
        return self.listed

    def set_listed(self, listed):
        self.listed = listed

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate



def argument_parser():
    parser = ArgumentParser()
    return parser


def main(top_block_cls=variable_numports_handler, options=None):
    if options is None:
        options = argument_parser().parse_args()

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
